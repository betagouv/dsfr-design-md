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
        # Special pairing: light=blue-france-975 (pale), dark=blue-france-sun-113
        # (saturated brand blue). Used by the `text-inverted-blue-france`
        # decision token so that "inverted" text on a Bleu France background
        # remains the brand blue when the page is in dark mode.
        ("blue-france-975-sun-113",    ("#f5f5fe", "#000091"), None, None),
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
        # DSFR docs ordering: main → strong → 1000 → 975 → 950 → 925 → 900 → 850.
        # `main`, `925-125`, `900-175` and `850-200` are static per the
        # canonical CSS; only `1000-50`, `975-100`, `950-150` (background
        # shades) and `200-850` (interactive text) expose hover/active.
        # The user-screenshot 8-shade set comes first, then the
        # additional decision-supporting shades our YAML also exposes.
        ("grey-main-525", ("#7b7b7b", "#7b7b7b"), None, None),
        ("grey-425-625",  ("#666666", "#929292"), None, None),
        ("grey-1000-50",  ("#ffffff", "#161616"),
                          ("#f6f6f6", "#343434"),
                          ("#ededed", "#474747")),
        ("grey-975-100",  ("#f6f6f6", "#242424"),
                          ("#dfdfdf", "#474747"),
                          ("#cfcfcf", "#5b5b5b")),
        # Canonical decision-token target for `background-alt-grey`.
        ("grey-975-75",   ("#f6f6f6", "#1e1e1e"),
                          ("#dfdfdf", "#3f3f3f"),
                          ("#cfcfcf", "#525252")),
        ("grey-950-150",  ("#eeeeee", "#2f2f2f"),
                          ("#d2d2d2", "#545454"),
                          ("#c1c1c1", "#696969")),
        # Canonical decision-token target for `background-contrast-grey`.
        ("grey-950-100",  ("#eeeeee", "#242424"),
                          ("#d2d2d2", "#474747"),
                          ("#c1c1c1", "#5b5b5b")),
        ("grey-925-125",  ("#e5e5e5", "#2a2a2a"), None, None),
        ("grey-900-175",  ("#dddddd", "#353535"), None, None),
        ("grey-850-200",  ("#cecece", "#3a3a3a"), None, None),
        # Additional shades exposed in our YAML, used by decision tokens:
        ("grey-625-425",  ("#929292", "#666666"), None, None),
        ("grey-200-850",  ("#3a3a3a", "#cecece"),
                          ("#616161", "#a8a8a8"),
                          ("#777777", "#939393")),
        ("grey-50-1000",  ("#161616", "#ffffff"), None, None),
        ("grey-0-1000",   ("#000000", "#ffffff"), None, None),
    ],
    # Système : ordre des familles imposé par la doc DSFR :
    # « Les couleurs systèmes sont : Info, warning, error, success. »
    # Au sein de chaque famille, ordre canonique (cf. en-tête PALETTE) :
    # main → strong → lightest → lighter → light → softest.
    #
    # NB : `*-main-525`, `*-925-125` et `*-850-200` ne sont pas exposés
    # comme variables CSS dans la distribution `dsfr.css` ; ce sont des
    # valeurs de référence de la documentation. Mêmes traitement que
    # `blue-france-main-525`, `grey-main-525`, `grey-925-125`,
    # `grey-850-200` : exposés sans hover/active dans nos previews.
    "Système · feedback fonctionnel": [
        # info
        ("info-main-525",    ("#0078f3", "#0078f3"), None, None),
        ("info-425-625",     ("#0063cb", "#518fff"), ("#3b87ff", "#98b4ff"), ("#6798ff", "#b4c7ff")),
        ("info-975-75",      ("#f4f6ff", "#171d2e"), None, None),
        ("info-950-100",     ("#e8edff", "#1d2437"), ("#c2d1ff", "#3b4767"), ("#a9bfff", "#4c5b83")),
        ("info-925-125",     ("#dde5ff", "#222a3f"), None, None),
        ("info-850-200",     ("#bccdff", "#273961"), None, None),
        # warning
        ("warning-main-525", ("#d64d00", "#d64d00"), None, None),
        ("warning-425-625",  ("#b34000", "#fc5d00"), ("#ff6218", "#ff8c73"), ("#ff7a55", "#ffa595")),
        ("warning-975-75",   ("#fff4f3", "#2d1814"), None, None),
        ("warning-950-100",  ("#ffe9e6", "#361e19"), ("#ffc6bd", "#663d35"), ("#ffb0a2", "#824f44")),
        ("warning-925-125",  ("#ffded9", "#3e231e"), None, None),
        ("warning-850-200",  ("#ffbeb4", "#5d2c20"), None, None),
        # error
        ("error-main-525",   ("#f60700", "#f60700"), None, None),
        ("error-425-625",    ("#ce0500", "#ff5655"), ("#ff2725", "#ff8c8c"), ("#ff4140", "#ffa6a6")),
        ("error-975-75",     ("#fff4f4", "#301717"), None, None),
        ("error-950-100",    ("#ffe9e9", "#391c1c"), ("#ffc5c5", "#6c3a3a"), ("#ffafaf", "#894b4b")),
        ("error-925-125",    ("#ffdddd", "#412121"), None, None),
        ("error-850-200",    ("#ffbdbd", "#642626"), None, None),
        # success
        ("success-main-525", ("#1f8d49", "#1f8d49"), None, None),
        ("success-425-625",  ("#18753c", "#27a658"), ("#27a959", "#36d975"), ("#2fc368", "#3df183")),
        ("success-975-75",   ("#dffee6", "#142117"), None, None),
        ("success-950-100",  ("#b8fec9", "#19271d"), ("#46fd89", "#344c3b"), ("#34eb7b", "#44624d")),
        ("success-925-125",  ("#88fdaa", "#1e2e22"), None, None),
        ("success-850-200",  ("#3bea7e", "#204129"), None, None),
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

# Decision tokens — curated subset for the visual mapping table. The full
# Tier 1+2 set (~78 tokens) lives in DESIGN.md; this list shows the most
# heavily-used decisions across each role so the preview stays scannable.
# Names follow the canonical DSFR convention: <role>-<level>-<family>.
DECISION_TOKENS_LIGHT = [
    # background
    ("background-default-grey",                "grey-1000-50",                "#ffffff"),
    ("background-alt-grey",                    "grey-975-75",                 "#f6f6f6"),
    ("background-contrast-grey",               "grey-950-100",                "#eeeeee"),
    ("background-action-high-blue-france",     "blue-france-sun-113-625",     "#000091"),
    ("background-action-low-blue-france",      "blue-france-925-125",         "#e3e3fd"),
    ("background-disabled-grey",               "grey-925-125",                "#e5e5e5"),
    # text
    ("text-default-grey",                      "grey-200-850",                "#3a3a3a"),
    ("text-title-grey",                        "grey-50-1000",                "#161616"),
    ("text-mention-grey",                      "grey-425-625",                "#666666"),
    ("text-action-high-blue-france",           "blue-france-sun-113-625",     "#000091"),
    ("text-inverted-blue-france",              "blue-france-975-sun-113",     "#f5f5fe"),
    ("text-disabled-grey",                     "grey-625-425",                "#929292"),
    # border
    ("border-default-grey",                    "grey-900-175",                "#dddddd"),
    ("border-plain-grey",                      "grey-200-850",                "#3a3a3a"),
    ("border-plain-success",                   "success-425-625",             "#18753c"),
    ("border-plain-warning",                   "warning-425-625",             "#b34000"),
    ("border-plain-error",                     "error-425-625",               "#ce0500"),
    ("border-plain-info",                      "info-425-625",                "#0063cb"),
    # literal
    ("focus-ring",                             "(literal)",                   "#0a76f6"),
]
DECISION_TOKENS_DARK = [
    # background
    ("background-default-grey",                "grey-1000-50",                "#161616"),
    ("background-alt-grey",                    "grey-975-75",                 "#1e1e1e"),
    ("background-contrast-grey",               "grey-950-100",                "#242424"),
    ("background-action-high-blue-france",     "blue-france-sun-113-625",     "#8585f6"),
    ("background-action-low-blue-france",      "blue-france-925-125",         "#272747"),
    ("background-disabled-grey",               "grey-925-125",                "#2a2a2a"),
    # text
    ("text-default-grey",                      "grey-200-850",                "#cecece"),
    ("text-title-grey",                        "grey-50-1000",                "#ffffff"),
    ("text-mention-grey",                      "grey-425-625",                "#929292"),
    ("text-action-high-blue-france",           "blue-france-sun-113-625",     "#8585f6"),
    ("text-inverted-blue-france",              "blue-france-975-sun-113",     "#000091"),
    ("text-disabled-grey",                     "grey-625-425",                "#666666"),
    # border
    ("border-default-grey",                    "grey-900-175",                "#353535"),
    ("border-plain-grey",                      "grey-200-850",                "#cecece"),
    ("border-plain-success",                   "success-425-625",             "#27a658"),
    ("border-plain-warning",                   "warning-425-625",             "#fc5d00"),
    ("border-plain-error",                     "error-425-625",               "#ff5655"),
    ("border-plain-info",                      "info-425-625",                "#518fff"),
    # literal
    ("focus-ring",                             "(literal)",                   "#4ea7ff"),
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


def hex_to_rgb(h: str) -> tuple[int, int, int]:
    """`#abc` or `#aabbcc` → (r, g, b)."""
    h = h.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)


def hex_to_hsl(h: str) -> tuple[int, float, float]:
    """`#abc` or `#aabbcc` → (hue°, saturation%, lightness%)."""
    r, g, b = (c / 255 for c in hex_to_rgb(h))
    mx, mn = max(r, g, b), min(r, g, b)
    l = (mx + mn) / 2
    if mx == mn:
        return 0, 0.0, round(l * 100, 1)
    d = mx - mn
    s = d / (2 - mx - mn) if l > 0.5 else d / (mx + mn)
    if mx == r:
        hue = ((g - b) / d) + (6 if g < b else 0)
    elif mx == g:
        hue = (b - r) / d + 2
    else:
        hue = (r - g) / d + 4
    return round(hue * 60), round(s * 100, 1), round(l * 100, 1)


def fmt_rgb(h: str) -> str:
    r, g, b = hex_to_rgb(h)
    return f"rgb({r},{g},{b})"


def fmt_hsl(h: str) -> str:
    deg, s, l = hex_to_hsl(h)
    # Trailing-zero strip to match DSFR's "85.8%" / "100%" formatting.
    s_str = f"{s:g}"
    l_str = f"{l:g}"
    return f"hsl({deg}deg {s_str}% {l_str}%)"


def shade_card(token: str, default: tuple[str, str], hover, active, scheme: str) -> str:
    """One card per shade, mirroring the DSFR docs' `.box-sample`.

    Layout: hero swatch (top), token name (bold), hex/rgb/hsl stacked,
    then an optional 2-cell hover/active sub-bar with hex/rgb only.
    All values use `<span>` (not `<code>`) so the global `code` styling
    in preview.html doesn't render them as grey pills.
    """
    idx = 0 if scheme == "light" else 1
    hex_val = default[idx]
    parts: list[str] = []
    parts.append('<div class="shade">')
    parts.append(f'  <span class="hero" style="background:var(--c-{token})"></span>')
    parts.append(f'  <b class="name">{token}</b>')
    parts.append(f'  <span class="hex">{hex_val}</span>')
    parts.append(f'  <span class="rgb">{fmt_rgb(hex_val)}</span>')
    parts.append(f'  <span class="hsl">{fmt_hsl(hex_val)}</span>')
    if hover or active:
        parts.append('  <div class="states-row">')
        for label, pair in (("hover", hover), ("active", active)):
            if not pair:
                continue
            v = pair[idx]
            parts.append(
                f'    <div class="state-cell">'
                f'<span class="bar" style="background:var(--c-{token}-{label})"></span>'
                f'<b>{label}</b>'
                f'<span class="hex">{v}</span>'
                f'<span class="rgb">{fmt_rgb(v)}</span>'
                f'</div>'
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
