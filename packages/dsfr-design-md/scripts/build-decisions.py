#!/usr/bin/env python3
"""Generate the canonical decision-tokens YAML block for DESIGN.md.

The DSFR's compiled `dsfr.css` contains ~600 CSS custom properties
that act as **decision tokens** — semantic names like
`--background-action-high-blue-france` that resolve (via `var()`) to
**option tokens** like `--blue-france-sun-113-625`. Most are part of
the role × level × family cartesian product and are never actually
used by any component.

This script:

  1. Fetches the canonical compiled `dsfr.css`.
  2. Parses every `--<role>-…: var(--<option>)` declaration in
     `:root` (decision tokens are theme-stable in name; the option
     token they reference handles light/dark switching).
  3. Counts `var(--<token>)` usage in component CSS (everything
     outside the `:root` blocks).
  4. Aggregates `-hover` / `-active` variant usage onto the base
     token, so a base + its variants share a single tier.
  5. Filters to **Tier 1 + Tier 2** (≥ 5 references in real
     component CSS) — covers ~73% of all decision-token references
     while skipping the ~272 unused dead-matrix tokens and the
     ~274 rarely-used Tier 3 tokens.
  6. Emits a grouped YAML block (by role, then alphabetically
     within role) ready to paste into DESIGN.md's `colors:` block.

Run from repo root:

    python3 scripts/build-decisions.py > /tmp/decisions.yaml

Or print to stdout for inspection:

    python3 scripts/build-decisions.py | less

The output is deterministic — same DSFR version + same threshold
produces the same YAML byte-for-byte. (Eventual `--check` mode
will compare regenerated output against DESIGN.md and exit 1 on
drift; deferred to the CI workflows plan.)
"""
from __future__ import annotations

import argparse
import re
import sys
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path
from dsfr_version import DSFR_VERSION, DSFR_CSS_URL

# ---------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------

ROLE_PREFIXES = ("background-", "text-", "border-", "artwork-")
DEFAULT_THRESHOLD = 5     # Tier 1+2

# Canonical role ordering for output. Mirrors `_decisions.scss`.
ROLE_ORDER = ("background", "text", "border", "artwork")

# Tokens documented on the DSFR canonical reference page
# (https://www.systeme-de-design.gouv.fr/version-courante/fr/fondamentaux/couleurs-palette).
# These are the user-facing decision tokens and must ALWAYS be emitted
# regardless of usage count — some of them appear only 1-2× in the
# canonical CSS yet are part of the public API. The whitelist applies
# to base names only; their `-hover` / `-active` variants are pulled
# in automatically by `tier_filter` if they exist in the canonical
# decisions dict.
# Doc-only decision tokens — names that appear on the DSFR canonical
# documentation page but are NOT compiled to a `--<name>: var(--…)`
# declaration in `:root`. The DSFR's SCSS resolves these at build
# time so components reference the option token directly. We add
# them here so DESIGN.md exposes the documented decision-token
# vocabulary even when the compiled CSS doesn't.
SYNTHETIC_DECISIONS: dict[str, str] = {
    "background-elevated-grey": "grey-1000-75",
    "background-contrast-raised-grey": "grey-950-125",
    "background-contrast-raised-grey-hover": "grey-950-125-hover",
    "background-contrast-raised-grey-active": "grey-950-125-active",
}

ALWAYS_INCLUDE = frozenset({
    # background (14)
    "background-alt-grey", "background-alt-blue-france",
    "background-contrast-grey", "background-elevated-grey",
    "background-action-high-blue-france", "background-action-low-blue-france",
    "background-active-blue-france", "background-open-blue-france",
    "background-disabled-grey",
    "background-flat-error", "background-flat-warning",
    "background-flat-success", "background-flat-info",
    "background-default-grey",
    # text (14)
    "text-title-grey", "text-title-blue-france",
    "text-default-grey", "text-mention-grey", "text-label-grey",
    "text-action-high-blue-france", "text-action-high-grey",
    "text-inverted-grey", "text-inverted-blue-france",
    "text-active-blue-france", "text-active-grey",
    "text-disabled-grey",
    "text-default-error", "text-default-success",
    # artwork (2)
    "artwork-major-blue-france", "artwork-minor-blue-france",
})


# ---------------------------------------------------------------------
# Fetch
# ---------------------------------------------------------------------

def fetch_css() -> str:
    """Fetch dsfr.css from jsdelivr (uses local /tmp cache if present)."""
    cache = Path(f"/tmp/dsfr-{DSFR_VERSION}.css")
    if cache.exists():
        return cache.read_text()
    with urllib.request.urlopen(DSFR_CSS_URL) as r:
        text = r.read().decode("utf-8")
    cache.write_text(text)
    return text


# ---------------------------------------------------------------------
# Parse
# ---------------------------------------------------------------------

def strip_root_blocks(css: str) -> str:
    """Remove every `:root { … }` and `:root[…] { … }` block.

    The leftover string is component CSS — i.e. real usage of tokens.
    Brace-depth tracking handles nested `@media`/`@supports` blocks
    correctly without choking on unbalanced braces inside strings
    (DSFR doesn't have any but we're defensive).
    """
    out: list[str] = []
    i, n = 0, len(css)
    pat = re.compile(r":root(?:\[[^\]]*\])?\s*\{")
    while i < n:
        m = pat.search(css, i)
        if not m:
            out.append(css[i:])
            break
        out.append(css[i:m.start()])
        depth, j = 1, m.end()
        while j < n and depth:
            depth += {"{": 1, "}": -1}.get(css[j], 0)
            j += 1
        i = j
    return "".join(out)


def extract_decisions(css: str) -> dict[str, str]:
    """Map decision-token name → referenced option-token name.

    Only includes declarations that actually point at an option token
    (i.e. `var(--…)`); literal-hex declarations like `--focus-ring:
    #0a76f6;` are excluded because they don't translate to a token
    reference in DESIGN.md.
    """
    decisions: dict[str, str] = {}
    pat = re.compile(r"--([a-z][a-z0-9-]+)\s*:\s*var\(--([a-z][a-z0-9-]+)\)")
    for m in pat.finditer(css):
        name, target = m.group(1), m.group(2)
        if name.startswith(ROLE_PREFIXES):
            decisions[name] = target
    return decisions


def compute_usage(component_css: str, declared: set[str]) -> Counter[str]:
    """Count `var(--<token>)` references in component CSS.

    Only references to declared decision tokens are counted; references
    to option tokens directly are ignored (we're tiering decision
    tokens, not options).
    """
    usage: Counter[str] = Counter()
    for m in re.finditer(r"var\(--([a-z][a-z0-9-]+)", component_css):
        if m.group(1) in declared:
            usage[m.group(1)] += 1
    return usage


def base_name(token: str) -> str:
    """Strip a `-hover` / `-active` suffix to recover the base token."""
    for suf in ("-hover", "-active"):
        if token.endswith(suf):
            return token[: -len(suf)]
    return token


# ---------------------------------------------------------------------
# Tier and group
# ---------------------------------------------------------------------

def tier_filter(
    decisions: dict[str, str],
    usage: Counter[str],
    threshold: int,
    always_include: frozenset[str] = ALWAYS_INCLUDE,
) -> list[str]:
    """Return the subset of decision-token names to emit.

    A token passes if either:
      - its **base** token is in `always_include` (the DSFR-doc whitelist
        of user-facing decision tokens), OR
      - its base token's aggregated usage is at or above `threshold`.

    `-hover` and `-active` variants inherit their base's status so we
    don't end up emitting an `-active` without its base or vice versa.
    """
    base_usage: Counter[str] = Counter()
    for tok in decisions:
        base_usage[base_name(tok)] += usage.get(tok, 0)
    return sorted(
        tok for tok in decisions
        if base_name(tok) in always_include
        or base_usage[base_name(tok)] >= threshold
    )


def group_by_role(tokens: list[str]) -> dict[str, list[str]]:
    """Group tokens by their role prefix; preserve sort order within."""
    grouped: dict[str, list[str]] = defaultdict(list)
    for tok in tokens:
        role = tok.split("-", 1)[0]
        grouped[role].append(tok)
    # Re-order roles canonically (background → text → border → artwork)
    return {r: grouped[r] for r in ROLE_ORDER if r in grouped}


# ---------------------------------------------------------------------
# Emit
# ---------------------------------------------------------------------

def load_palette_options(build_previews_path: Path) -> set[str]:
    """Discover which option-token names exist in our PALETTE.

    Reads `scripts/build-previews.py` and extracts every option-token
    name plus its `-hover` / `-active` variants. We only emit decision
    tokens whose target exists, so DESIGN.md stays self-consistent.
    """
    src = build_previews_path.read_text()
    options: set[str] = set()
    for m in re.finditer(r'\(\s*"([a-z][a-z0-9-]+)"\s*,\s*\("#', src):
        name = m.group(1)
        options.add(name)
        options.add(name + "-hover")
        options.add(name + "-active")
    return options


def emit_yaml(
    grouped: dict[str, list[str]],
    decisions: dict[str, str],
    usage: Counter[str],
    available_options: set[str] | None,
) -> tuple[str, list[str]]:
    """Render the YAML block with role headers and aligned columns.

    Returns `(yaml_text, skipped_tokens)`. A decision token is skipped
    when its option-token target isn't present in `available_options`
    (preserving self-consistency of the resulting DESIGN.md). When
    `available_options` is None, no filtering is applied.
    """
    skipped: list[str] = []
    kept_grouped: dict[str, list[str]] = {}
    for role, toks in grouped.items():
        kept_grouped[role] = []
        for tok in toks:
            target = decisions[tok]
            if available_options is not None and target not in available_options:
                skipped.append(f"{tok} -> {target}")
                continue
            kept_grouped[role].append(tok)
    # Drop empty roles
    kept_grouped = {r: ts for r, ts in kept_grouped.items() if ts}

    lines: list[str] = []
    lines.append(
        f"  # DECISION TOKENS — generated by `scripts/build-decisions.py`\n"
        f"  # Source: @gouvfr/dsfr@{DSFR_VERSION}/dist/dsfr.css\n"
        f"  # Tier 1+2 (≥{DEFAULT_THRESHOLD} component-CSS references). Do not\n"
        f"  # edit by hand — re-run the script and paste the output."
    )

    all_toks = [t for toks in kept_grouped.values() for t in toks]
    if not all_toks:
        return "\n".join(lines) + "\n", skipped
    width = max(len(t) for t in all_toks) + 2  # +2 for ": "

    for role, toks in kept_grouped.items():
        lines.append(f"\n  # ---- {role} ----")
        for tok in toks:
            target = decisions[tok]
            n = usage.get(tok, 0)
            key = f"{tok}:"
            lines.append(f'  {key:<{width}}"{{colors.{target}}}"   # used {n}×')
    return "\n".join(lines) + "\n", skipped


# ---------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument(
        "--threshold", type=int, default=DEFAULT_THRESHOLD,
        help=f"Min component-CSS references to emit a token (default: {DEFAULT_THRESHOLD})"
    )
    parser.add_argument(
        "--no-filter-options", action="store_true",
        help=("Don't filter to PALETTE-available option tokens. "
              "Useful for surveying the full canonical decision set."),
    )
    parser.add_argument(
        "--summary", action="store_true",
        help="Print a summary line to stderr after generating",
    )
    args = parser.parse_args()

    css = fetch_css()
    decisions = extract_decisions(css)
    # Merge in the doc-only decisions that don't appear in compiled CSS
    # but are part of the public DSFR API (e.g. background-elevated-grey).
    for tok, target in SYNTHETIC_DECISIONS.items():
        decisions.setdefault(tok, target)
    component = strip_root_blocks(css)
    usage = compute_usage(component, set(decisions))

    selected = tier_filter(decisions, usage, args.threshold)
    grouped = group_by_role(selected)

    available = None
    if not args.no_filter_options:
        # Discover available option tokens from build-previews.py
        # (script lives alongside us in scripts/).
        here = Path(__file__).resolve().parent
        available = load_palette_options(here / "build-previews.py")

    yaml, skipped = emit_yaml(grouped, decisions, usage, available)
    sys.stdout.write(yaml)

    if args.summary:
        total_decisions = len(decisions)
        emitted = len(selected) - len(skipped)
        ref_total = sum(usage.values())
        kept = {tok for toks in group_by_role(selected).values() for tok in toks
                if available is None or decisions[tok] in available}
        ref_covered = sum(usage[t] for t in kept)
        cov = ref_covered / ref_total * 100 if ref_total else 0
        print(
            f"\n  # Summary: emitted {emitted}/{total_decisions} decision tokens "
            f"(threshold ≥{args.threshold}) covering {cov:.0f}% of all "
            f"component-CSS decision-token references.",
            file=sys.stderr,
        )
        if skipped:
            print(
                f"  # Skipped {len(skipped)} decisions whose option-token target "
                f"isn't in PALETTE; pass --no-filter-options to inspect them.",
                file=sys.stderr,
            )
    return 0


if __name__ == "__main__":
    sys.exit(main())
