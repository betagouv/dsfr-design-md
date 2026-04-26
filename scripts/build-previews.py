#!/usr/bin/env python3
"""Regenerate preview.html and preview-dark.html from the token data below.

This script is the source of truth for the colour swatch grids and the
CSS custom properties block in the two preview files. Everything else
in the previews (typography, spacing, components, etc.) is hand-written
HTML left untouched by this script — the swatch grids and :root token
block are the only things regenerated.

Run from the repo root:

    python3 scripts/build-previews.py

Token values are mirrored from @gouvfr/dsfr@1.13.0/dist/dsfr.css.
"""
from __future__ import annotations
import re
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# ---------------------------------------------------------------------
# Canonical DSFR option-token values, light + dark.
# Keys map directly to the names in DESIGN.md's YAML.
# ---------------------------------------------------------------------
# Tuple shape: (light, dark) — None if a token is theme-stable.

#
# Ordering convention (mirrors the DSFR documentation site's palette pages):
#
#   1. main         (reference colour, no -hover/-active)
#   2. strong       (saturated interactive shade — `sun-113-625` for Bleu
#                    France, `425-625` for the rest)
#   3. lightest     (`-975-75`)
#   4. lighter      (`-950-100`)
#   5. light        (`-925-125`)
#   6. softest      (`-850-200`)
#
# i.e. main → strong → tints lightest-to-darkest. This is *not* numeric
# order; it's the design-system reading order used by the DSFR docs.
PALETTE = {
    "Bleu France · marque primaire": [
        # name, default L/D, hover L/D or None, active L/D or None
        ("blue-france-main-525",       ("#6a6af4", "#6a6af4"), None, None),
        ("blue-france-sun-113-625",    ("#000091", "#8585f6"), ("#1212ff", "#b1b1f9"), ("#2323ff", "#c6c6fb")),
        ("blue-france-975-75",         ("#f5f5fe", "#1b1b35"), ("#dcdcfc", "#3a3a68"), ("#cbcbfa", "#4d4d83")),
        ("blue-france-950-100",        ("#ececfe", "#21213f"), ("#cecefc", "#424275"), ("#bbbbfc", "#56568c")),
        ("blue-france-925-125",        ("#e3e3fd", "#272747"), ("#c1c1fb", "#4a4a7d"), ("#adadf9", "#5e5e90")),
        ("blue-france-850-200",        ("#cacafb", "#313178"), None, None),
    ],
    "Rouge Marianne": [
        ("red-marianne-main-472",      ("#e1000f", "#e1000f"), None, None),
        ("red-marianne-425-625",       ("#c9191e", "#f95c5e"), ("#f93f42", "#fa9293"), ("#f95a5c", "#fbabac")),
        ("red-marianne-975-75",        ("#fef4f4", "#2b1919"), ("#fcd7d7", "#573737"), ("#fac4c4", "#704848")),
        ("red-marianne-950-100",       ("#fee9e9", "#331f1f"), ("#fdc5c5", "#613f3f"), ("#fcafaf", "#7b5151")),
        ("red-marianne-925-125",       ("#fddede", "#3b2424"), ("#fbb6b6", "#6b4545"), ("#fa9e9e", "#865757")),
        ("red-marianne-850-200",       ("#fcbfbf", "#5e2a2b"), None, None),
    ],
    "Neutres · orientation thème clair": [
        ("grey-1000-50",  ("#ffffff", "#161616"), None, None),
        ("grey-975-100",  ("#f6f6f6", "#1e1e1e"), None, None),
        ("grey-950-150",  ("#eeeeee", "#2a2a2a"), None, None),
        ("grey-900-175",  ("#e5e5e5", "#353535"), None, None),
        ("grey-850-200",  ("#dddddd", "#3a3a3a"), None, None),
        ("grey-625-425",  ("#929292", "#666666"), None, None),
        ("grey-425-625",  ("#666666", "#929292"), None, None),
        ("grey-200-850",  ("#3a3a3a", "#cecece"), None, None),
        ("grey-50-1000",  ("#161616", "#f5f5f5"), None, None),
        ("grey-0-1000",   ("#000000", "#ffffff"), None, None),
    ],
    "Système · feedback fonctionnel": [
        ("success-425-625", ("#18753c", "#27a658"), ("#27a959", "#36d975"), ("#2fc368", "#3df183")),
        ("success-950-100", ("#b8fec9", "#19271d"), ("#46fd89", "#344c3b"), ("#34eb7b", "#44624d")),
        ("success-975-75",  ("#dffee6", "#142117"), None, None),
        ("warning-425-625", ("#b34000", "#fc5d00"), ("#ff6218", "#ff8c73"), ("#ff7a55", "#ffa595")),
        ("warning-950-100", ("#ffe9e6", "#361e19"), ("#ffc6bd", "#663d35"), ("#ffb0a2", "#824f44")),
        ("warning-975-75",  ("#fff4f3", "#2d1814"), None, None),
        ("error-425-625",   ("#ce0500", "#ff5655"), ("#ff2725", "#ff8c8c"), ("#ff4140", "#ffa6a6")),
        ("error-950-100",   ("#ffe9e9", "#391c1c"), ("#ffc5c5", "#6c3a3a"), ("#ffafaf", "#894b4b")),
        ("error-975-75",    ("#fff4f4", "#301717"), None, None),
        ("info-425-625",    ("#0063cb", "#518fff"), ("#3b87ff", "#98b4ff"), ("#6798ff", "#b4c7ff")),
        ("info-950-100",    ("#e8edff", "#1d2437"), ("#c2d1ff", "#3b4767"), ("#a9bfff", "#4c5b83")),
        ("info-975-75",     ("#f4f6ff", "#171d2e"), None, None),
    ],
    "Accents illustratifs · une famille par page": [
        # Illustrative accents have no documented hover/active in the CSS dist.
        ("green-tilleul-verveine-main-707", ("#b7a73f", "#b7a73f"), None, None),
        ("green-bourgeon-main-640",         ("#68a532", "#68a532"), None, None),
        ("green-emeraude-main-632",         ("#00a95f", "#00a95f"), None, None),
        ("green-menthe-main-548",           ("#009081", "#009081"), None, None),
        ("green-archipel-main-557",         ("#009099", "#009099"), None, None),
        ("blue-ecume-main-400",             ("#465f9d", "#465f9d"), None, None),
        ("blue-cumulus-main-526",           ("#417dc4", "#417dc4"), None, None),
        ("purple-glycine-main-494",         ("#a558a0", "#a558a0"), None, None),
        ("pink-macaron-main-689",           ("#e18b76", "#e18b76"), None, None),
        ("pink-tuile-main-556",             ("#ce614a", "#ce614a"), None, None),
        ("yellow-tournesol-main-731",       ("#c8aa39", "#c8aa39"), None, None),
        ("yellow-moutarde-main-679",        ("#c3992a", "#c3992a"), None, None),
        ("orange-terre-battue-main-645",    ("#e4794a", "#e4794a"), None, None),
        ("brown-cafe-creme-main-782",       ("#d1b781", "#d1b781"), None, None),
        ("brown-caramel-main-648",          ("#c08c65", "#c08c65"), None, None),
        ("brown-opera-main-680",            ("#bd987a", "#bd987a"), None, None),
        ("beige-gris-galet-main-702",       ("#aea397", "#aea397"), None, None),
    ],
}

# Decision tokens that depend on option tokens. Listed for the mapping table.
DECISION_TOKENS_LIGHT = [
    ("primary",                          "blue-france-sun-113-625",  "#000091"),
    ("primary-hover",                    "blue-france-sun-113-625-hover", "#1212ff"),
    ("primary-active",                   "blue-france-sun-113-625-active", "#2323ff"),
    ("on-primary",                       "grey-1000-50",             "#ffffff"),
    ("background-default",               "grey-1000-50",             "#ffffff"),
    ("background-alt",                   "grey-975-100",             "#f6f6f6"),
    ("background-contrast-grey",         "grey-950-150",             "#eeeeee"),
    ("background-action-low-blue-france","blue-france-925-125",      "#e3e3fd"),
    ("text-default-grey",                "grey-50-1000",             "#161616"),
    ("text-mention-grey",                "grey-425-625",             "#666666"),
    ("text-action-high-blue-france",     "blue-france-sun-113-625",  "#000091"),
    ("border-default-grey",              "grey-900-175",             "#e5e5e5"),
    ("focus-ring",                       "(literal)",                "#0a76f6"),
]
DECISION_TOKENS_DARK = [
    ("primary",                          "blue-france-sun-113-625",  "#8585f6"),
    ("primary-hover",                    "blue-france-sun-113-625-hover", "#b1b1f9"),
    ("primary-active",                   "blue-france-sun-113-625-active", "#c6c6fb"),
    ("on-primary",                       "(constant)",               "#1b1b35"),
    ("background-default",               "grey-1000-50",             "#161616"),
    ("background-alt",                   "grey-975-100",             "#1e1e1e"),
    ("background-contrast-grey",         "grey-950-150",             "#2a2a2a"),
    ("background-action-low-blue-france","blue-france-925-125",      "#272747"),
    ("text-default-grey",                "grey-50-1000",             "#f5f5f5"),
    ("text-mention-grey",                "grey-425-625",             "#929292"),
    ("text-action-high-blue-france",     "blue-france-sun-113-625",  "#8585f6"),
    ("border-default-grey",              "grey-900-175",             "#353535"),
    ("focus-ring",                       "(literal)",                "#4ea7ff"),
]


# ---------------------------------------------------------------------
# Generators
# ---------------------------------------------------------------------

def css_var_block(scheme: str) -> str:
    """Emit the :root { --c-... } block with all option tokens flattened."""
    idx = 0 if scheme == "light" else 1
    lines: list[str] = []
    for group_name, shades in PALETTE.items():
        lines.append(f"      /* ---- {group_name} ---- */")
        for token, default, hover, active in shades:
            lines.append(f"      --c-{token}:        {default[idx]};")
            if hover:
                lines.append(f"      --c-{token}-hover:  {hover[idx]};")
            if active:
                lines.append(f"      --c-{token}-active: {active[idx]};")
        lines.append("")
    return "\n".join(lines).rstrip()


def short_label(token: str) -> str:
    """Display name for a token (strip family prefix when verbose)."""
    return token


def shade_card(token: str, default: tuple[str, str], hover, active, scheme: str) -> str:
    """One card per shade: hero swatch + token name + hex + optional hover/active sub-bar."""
    idx = 0 if scheme == "light" else 1
    parts: list[str] = []
    parts.append('<div class="shade">')
    parts.append(f'  <div class="hero" style="background:var(--c-{token})"></div>')
    parts.append('  <div class="meta">')
    parts.append(f'    <b>{short_label(token)}</b>')
    parts.append(f'    <code class="hex">{default[idx]}</code>')
    parts.append('  </div>')
    if hover or active:
        parts.append('  <div class="states-row">')
        if hover:
            parts.append(
                f'    <div class="state-cell"><span class="bar" style="background:var(--c-{token}-hover)"></span>'
                f'<b>hover</b><code>{hover[idx]}</code></div>'
            )
        if active:
            parts.append(
                f'    <div class="state-cell"><span class="bar" style="background:var(--c-{token}-active)"></span>'
                f'<b>active</b><code>{active[idx]}</code></div>'
            )
        parts.append('  </div>')
    parts.append('</div>')
    return "\n      ".join(parts)


def colors_section_html(scheme: str) -> str:
    """Build the entire colors section content (everything between the
    section heading paragraph and the decision-tokens table)."""
    out: list[str] = []
    for group_name, shades in PALETTE.items():
        out.append(f'    <div class="group-label">{group_name}</div>')
        if "Accents illustratifs" in group_name:
            out.append('    <p class="muted" style="font-size:0.875rem;">')
            out.append('      Réservés à l\'éditorial. Jamais utilisés pour les actions ou les couleurs système.')
            out.append('    </p>')
        out.append('    <div class="shade-grid">')
        for token, default, hover, active in shades:
            out.append('      ' + shade_card(token, default, hover, active, scheme))
        out.append('    </div>')
        out.append('')
    return "\n".join(out)


def decision_table_html(scheme: str) -> str:
    rows = DECISION_TOKENS_LIGHT if scheme == "light" else DECISION_TOKENS_DARK
    label = "Pointe vers (clair)" if scheme == "light" else "Pointe vers (sombre)"
    out: list[str] = []
    out.append('    <h3>Tokens de décision</h3>')
    out.append('    <p>Les composants doivent référencer ces tokens, pas les options brutes.</p>')
    out.append('    <table class="tokens">')
    out.append('      <thead>')
    out.append(f'        <tr><th>Token de décision</th><th>{label}</th><th>Couleur</th></tr>')
    out.append('      </thead>')
    out.append('      <tbody>')
    for tok, points_at, hex_val in rows:
        # Use a literal hex for the decision-token preview so the table is
        # readable even if the var ref drifts during a refactor.
        out.append(
            f'        <tr><td class="tok">{tok}</td>'
            f'<td class="tok">{points_at}</td>'
            f'<td><span class="dot" style="background:{hex_val}"></span><code>{hex_val}</code></td></tr>'
        )
    out.append('      </tbody>')
    out.append('    </table>')
    return "\n".join(out)


# ---------------------------------------------------------------------
# Replace markers in source files
# ---------------------------------------------------------------------

def replace_block(src: str, start: str, end: str, replacement: str) -> str:
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.DOTALL)
    if not pattern.search(src):
        raise SystemExit(f"could not find block bounded by {start!r} … {end!r}")
    return pattern.sub(start + "\n" + replacement + "\n    " + end, src)


def regenerate(scheme: str) -> None:
    fname = "preview.html" if scheme == "light" else "preview-dark.html"
    path = ROOT / fname
    src = path.read_text()

    # 1. Replace the :root token block (between BEGIN/END markers).
    css = css_var_block(scheme)
    src = replace_block(
        src,
        "/* BEGIN GENERATED TOKENS */",
        "/* END GENERATED TOKENS */",
        textwrap.indent(css, ""),
    )

    # 2. Replace the colors-section body (between BEGIN/END markers).
    body = colors_section_html(scheme)
    src = replace_block(
        src,
        "<!-- BEGIN GENERATED COLORS -->",
        "<!-- END GENERATED COLORS -->",
        body,
    )

    # 3. Replace the decision-tokens table.
    table = decision_table_html(scheme)
    src = replace_block(
        src,
        "<!-- BEGIN GENERATED DECISION TABLE -->",
        "<!-- END GENERATED DECISION TABLE -->",
        table,
    )

    path.write_text(src)
    print(f"  ✓ {fname}")


def main() -> None:
    print("Regenerating previews from canonical token data:")
    regenerate("light")
    regenerate("dark")
    print("Done.")


if __name__ == "__main__":
    main()
