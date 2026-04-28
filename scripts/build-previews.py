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
        # Canonical decision-token target for `background-elevated-grey`.
        # Same light value as grey-1000-50 but darker dark value (grey-75
        # instead of grey-50) — used for raised surfaces like dropdowns
        # that need to read as "lifted" against the page in dark mode.
        ("grey-1000-75",  ("#ffffff", "#1e1e1e"),
                          ("#f6f6f6", "#3f3f3f"),
                          ("#ededed", "#525252")),
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
    # Système : couleurs fonctionnelles. Ordre des familles d'après les
    # captures de la doc DSFR : info → succès → avertissement → erreur.
    # Chaque famille obtient sa propre section visuelle (titre +
    # grille de 6 cartes), suivant les niveaux canoniques
    # main → strong → lightest → lighter → light → softest.
    #
    # NB : `*-main-525`, `*-925-125` et `*-850-200` ne sont pas exposés
    # comme variables CSS dans la distribution `dsfr.css` ; ce sont des
    # valeurs de référence de la documentation. Mêmes traitement que
    # `blue-france-main-525`, `grey-main-525`, `grey-925-125`,
    # `grey-850-200` : exposés sans hover/active dans nos previews.
    #
    # Le placeholder `{scheme_label}` est remplacé au rendu par
    # « (thème clair) » ou « (thème sombre) » selon la preview.
    "Info {scheme_label}": [
        ("info-main-525",    ("#0078f3", "#0078f3"), None, None),
        ("info-425-625",     ("#0063cb", "#518fff"), ("#3b87ff", "#98b4ff"), ("#6798ff", "#b4c7ff")),
        ("info-975-75",      ("#f4f6ff", "#171d2e"), None, None),
        ("info-950-100",     ("#e8edff", "#1d2437"), ("#c2d1ff", "#3b4767"), ("#a9bfff", "#4c5b83")),
        ("info-925-125",     ("#dde5ff", "#222a3f"), None, None),
        ("info-850-200",     ("#bccdff", "#273961"), None, None),
    ],
    "Succès {scheme_label}": [
        ("success-main-525", ("#1f8d49", "#1f8d49"), None, None),
        ("success-425-625",  ("#18753c", "#27a658"), ("#27a959", "#36d975"), ("#2fc368", "#3df183")),
        ("success-975-75",   ("#dffee6", "#142117"), None, None),
        ("success-950-100",  ("#b8fec9", "#19271d"), ("#46fd89", "#344c3b"), ("#34eb7b", "#44624d")),
        ("success-925-125",  ("#88fdaa", "#1e2e22"), None, None),
        ("success-850-200",  ("#3bea7e", "#204129"), None, None),
    ],
    "Avertissement {scheme_label}": [
        ("warning-main-525", ("#d64d00", "#d64d00"), None, None),
        ("warning-425-625",  ("#b34000", "#fc5d00"), ("#ff6218", "#ff8c73"), ("#ff7a55", "#ffa595")),
        ("warning-975-75",   ("#fff4f3", "#2d1814"), None, None),
        ("warning-950-100",  ("#ffe9e6", "#361e19"), ("#ffc6bd", "#663d35"), ("#ffb0a2", "#824f44")),
        ("warning-925-125",  ("#ffded9", "#3e231e"), None, None),
        ("warning-850-200",  ("#ffbeb4", "#5d2c20"), None, None),
    ],
    "Erreur {scheme_label}": [
        ("error-main-525",   ("#f60700", "#f60700"), None, None),
        ("error-425-625",    ("#ce0500", "#ff5655"), ("#ff2725", "#ff8c8c"), ("#ff4140", "#ffa6a6")),
        ("error-975-75",     ("#fff4f4", "#301717"), None, None),
        ("error-950-100",    ("#ffe9e9", "#391c1c"), ("#ffc5c5", "#6c3a3a"), ("#ffafaf", "#894b4b")),
        ("error-925-125",    ("#ffdddd", "#412121"), None, None),
        ("error-850-200",    ("#ffbdbd", "#642626"), None, None),
    ],
    # ----- Accents illustratifs -----
    # 17 familles, ordre de la doc DSFR :
    # Tilleul verveine, Bourgeon, Émeraude, Menthe, Archipel, Écume,
    # Cumulus, Glycine, Macaron, Tuile, Tournesol, Moutarde,
    # Terre battue, Café crème, Caramel, Opéra, Gris galet.
    #
    # Chaque famille suit la même structure de 6 nuances :
    #   main-XXX            référence (thème-stable, pas de hover/active)
    #   sun-XXX-moon-YYY    nuance forte (paire light/dark, hover/active)
    #   975-75              très clair (paire, hover/active)
    #   950-100             clair (paire, hover/active)
    #   925-125             intermédiaire (paire, hover/active)
    #   850-200             plus saturé (paire, pas de hover/active)
    "Tilleul verveine {scheme_label}": [
        ("green-tilleul-verveine-main-707", ("#b7a73f", "#b7a73f"), None, None),
        ("green-tilleul-verveine-sun-418-moon-817", ("#66673d", "#d8c634"), ("#929359", "#fee943"), ("#a7a967", "#fef1ab")),
        ("green-tilleul-verveine-975-75", ("#fef7da", "#201e14"), ("#fce552", "#433f2e"), ("#ebd54c", "#57533d")),
        ("green-tilleul-verveine-950-100", ("#fceeac", "#272419"), ("#e8d45c", "#4c4734"), ("#d4c254", "#615b44")),
        ("green-tilleul-verveine-925-125", ("#fbe769", "#2d2a1d"), ("#d7c655", "#534f39"), ("#c2b24c", "#696349")),
        ("green-tilleul-verveine-850-200", ("#e2cf58", "#3f3a20"), None, None),
    ],
    "Bourgeon {scheme_label}": [
        ("green-bourgeon-main-640", ("#68a532", "#68a532"), None, None),
        ("green-bourgeon-sun-425-moon-759", ("#447049", "#99c221"), ("#639f6a", "#baec2a"), ("#72b77a", "#c9fd2e")),
        ("green-bourgeon-975-75", ("#e6feda", "#182014"), ("#a7fc62", "#35432e"), ("#98ed4d", "#46573d")),
        ("green-bourgeon-950-100", ("#c9fcac", "#1e2719"), ("#9ae95d", "#3d4c34"), ("#8dd555", "#4e6144")),
        ("green-bourgeon-925-125", ("#a9fb68", "#232d1d"), ("#8ed654", "#435339"), ("#7fc04b", "#556949")),
        ("green-bourgeon-850-200", ("#95e257", "#2a401a"), None, None),
    ],
    "Émeraude {scheme_label}": [
        ("green-emeraude-main-632", ("#00a95f", "#00a95f"), None, None),
        ("green-emeraude-sun-425-moon-753", ("#297254", "#34cb6a"), ("#3ea47a", "#42fb84"), ("#49bc8d", "#80fda3")),
        ("green-emeraude-975-75", ("#e3fdeb", "#142018"), ("#94f9b9", "#2e4335"), ("#6df1a3", "#3d5846")),
        ("green-emeraude-950-100", ("#c3fad5", "#19271e"), ("#77eda5", "#344c3d"), ("#6dd897", "#44624f")),
        ("green-emeraude-925-125", ("#9ef9be", "#1e2e23"), ("#69df97", "#3b5543"), ("#5ec988", "#4b6b55")),
        ("green-emeraude-850-200", ("#6fe49d", "#21402c"), None, None),
    ],
    "Menthe {scheme_label}": [
        ("green-menthe-main-548", ("#009081", "#009081"), None, None),
        ("green-menthe-sun-373-moon-652", ("#37635f", "#21ab8e"), ("#53918c", "#2eddb8"), ("#62a9a2", "#34f4cc")),
        ("green-menthe-975-75", ("#dffdf7", "#15201e"), ("#84f9e7", "#30433f"), ("#70ebd8", "#3f5753")),
        ("green-menthe-950-100", ("#bafaee", "#1a2624"), ("#79e7d5", "#364b47"), ("#6fd3c3", "#46605b")),
        ("green-menthe-925-125", ("#8bf8e7", "#1f2d2a"), ("#6ed5c5", "#3c534e"), ("#62bfb1", "#4d6963")),
        ("green-menthe-850-200", ("#73e0cf", "#223f3a"), None, None),
    ],
    "Archipel {scheme_label}": [
        ("green-archipel-main-557", ("#009099", "#009099"), None, None),
        ("green-archipel-sun-391-moon-716", ("#006a6f", "#34bab5"), ("#009fa7", "#43e9e2"), ("#00bbc3", "#4cfdf6")),
        ("green-archipel-975-75", ("#e5fbfd", "#152021"), ("#99f2f8", "#2f4345"), ("#73e9f0", "#3f5759")),
        ("green-archipel-950-100", ("#c7f6fc", "#1a2628"), ("#64ecf8", "#364a4e"), ("#5bd8e3", "#465f63")),
        ("green-archipel-925-125", ("#a6f2fa", "#1f2c2e"), ("#62dbe5", "#3c5255"), ("#58c5cf", "#4d676b")),
        ("green-archipel-850-200", ("#60e0eb", "#233e41"), None, None),
    ],
    "Écume {scheme_label}": [
        ("blue-ecume-main-400", ("#465f9d", "#465f9d"), None, None),
        ("blue-ecume-sun-247-moon-675", ("#2f4077", "#869ece"), ("#4e68bb", "#b8c5e2"), ("#667dcf", "#ced6ea")),
        ("blue-ecume-975-75", ("#f4f6fe", "#171d2f"), ("#d7dffb", "#333e5e"), ("#c3cffa", "#445179")),
        ("blue-ecume-950-100", ("#e9edfe", "#1d2437"), ("#c5d0fc", "#3b4767"), ("#adbffc", "#4c5b83")),
        ("blue-ecume-925-125", ("#dee5fd", "#222940"), ("#b4c5fb", "#424d73"), ("#99b3f9", "#536190")),
        ("blue-ecume-850-200", ("#bfccfb", "#273962"), None, None),
    ],
    "Cumulus {scheme_label}": [
        ("blue-cumulus-main-526", ("#417dc4", "#417dc4"), None, None),
        ("blue-cumulus-sun-368-moon-732", ("#3558a2", "#7ab1e8"), ("#5982e0", "#bad2f2"), ("#7996e6", "#d2e2f6")),
        ("blue-cumulus-975-75", ("#f3f6fe", "#171e2b"), ("#d3dffc", "#333f56"), ("#bed0fa", "#43536f")),
        ("blue-cumulus-950-100", ("#e6eefe", "#1c2433"), ("#bcd3fc", "#3a4761"), ("#9fc3fc", "#4a5b7b")),
        ("blue-cumulus-925-125", ("#dae6fd", "#212a3a"), ("#a9c8fb", "#404f69"), ("#8ab8f9", "#516384")),
        ("blue-cumulus-850-200", ("#b6cffb", "#263b58"), None, None),
    ],
    "Glycine {scheme_label}": [
        ("purple-glycine-main-494", ("#a558a0", "#a558a0"), None, None),
        ("purple-glycine-sun-319-moon-630", ("#6e445a", "#ce70cc"), ("#a66989", "#dfa4dd"), ("#bb7f9e", "#e7bbe6")),
        ("purple-glycine-975-75", ("#fef3fd", "#251a24"), ("#fcd4f8", "#4c394a"), ("#fabff5", "#634a60")),
        ("purple-glycine-950-100", ("#fee7fc", "#2c202b"), ("#fdc0f8", "#554053"), ("#fca8f6", "#6c536a")),
        ("purple-glycine-925-125", ("#fddbfa", "#332632"), ("#fbaff5", "#5d485c"), ("#fa96f2", "#755b73")),
        ("purple-glycine-850-200", ("#fbb8f6", "#502e4d"), None, None),
    ],
    "Macaron {scheme_label}": [
        ("pink-macaron-main-689", ("#e18b76", "#e18b76"), None, None),
        ("pink-macaron-sun-406-moon-833", ("#8d533e", "#ffb7ae"), ("#ca795c", "#ffe0dc"), ("#e08e73", "#fff0ee")),
        ("pink-macaron-975-75", ("#fef4f2", "#261b19"), ("#fcd8d0", "#4e3a37"), ("#fac5b8", "#654c48")),
        ("pink-macaron-950-100", ("#fee9e6", "#2e211f"), ("#fdc6bd", "#58423f"), ("#fcb0a2", "#705551")),
        ("pink-macaron-925-125", ("#fddfda", "#352724"), ("#fbb8ab", "#614a45"), ("#faa18d", "#795d57")),
        ("pink-macaron-850-200", ("#fcc0b4", "#52312a"), None, None),
    ],
    "Tuile {scheme_label}": [
        ("pink-tuile-main-556", ("#ce614a", "#ce614a"), None, None),
        ("pink-tuile-sun-425-moon-750", ("#a94645", "#ff9575"), ("#d5706f", "#ffc4b7"), ("#da8a89", "#ffd8d0")),
        ("pink-tuile-975-75", ("#fef4f3", "#281b19"), ("#fcd7d3", "#513a37"), ("#fac4be", "#694c48")),
        ("pink-tuile-950-100", ("#fee9e7", "#2f211f"), ("#fdc6c0", "#5a423e"), ("#fcb0a7", "#725550")),
        ("pink-tuile-925-125", ("#fddfdb", "#372624"), ("#fbb8ad", "#644845"), ("#faa191", "#7d5b57")),
        ("pink-tuile-850-200", ("#fcbfb7", "#55302a"), None, None),
    ],
    "Tournesol {scheme_label}": [
        ("yellow-tournesol-main-731", ("#c8aa39", "#c8aa39"), None, None),
        ("yellow-tournesol-sun-407-moon-922", ("#716043", "#ffe552"), ("#a28a62", "#e1c700"), ("#ba9f72", "#cab300")),
        ("yellow-tournesol-975-75", ("#fef6e3", "#221d11"), ("#fce086", "#473e29"), ("#f5d24b", "#5c5136")),
        ("yellow-tournesol-950-100", ("#feecc2", "#292416"), ("#fbd335", "#4f472f"), ("#e6c130", "#655b3d")),
        ("yellow-tournesol-925-125", ("#fde39c", "#302a1a"), ("#e9c53b", "#584e34"), ("#d3b235", "#6f6342")),
        ("yellow-tournesol-850-200", ("#efcb3a", "#43391a"), None, None),
    ],
    "Moutarde {scheme_label}": [
        ("yellow-moutarde-main-679", ("#c3992a", "#c3992a"), None, None),
        ("yellow-moutarde-sun-348-moon-860", ("#695240", "#ffca00"), ("#9b7b61", "#cda200"), ("#b58f72", "#b28c00")),
        ("yellow-moutarde-975-75", ("#fef5e8", "#231d14"), ("#fcdca3", "#483e2e"), ("#fbcd64", "#5e513d")),
        ("yellow-moutarde-950-100", ("#feebd0", "#2a2319"), ("#fdcd6d", "#514534"), ("#f4be30", "#685944")),
        ("yellow-moutarde-925-125", ("#fde2b5", "#30291d"), ("#f6c43c", "#584d39"), ("#dfb135", "#6f6149")),
        ("yellow-moutarde-850-200", ("#fcc63a", "#453820"), None, None),
    ],
    "Terre battue {scheme_label}": [
        ("orange-terre-battue-main-645", ("#e4794a", "#e4794a"), None, None),
        ("orange-terre-battue-sun-370-moon-672", ("#755348", "#ff732c"), ("#ab7b6b", "#ffa48b"), ("#c68f7d", "#ffbbab")),
        ("orange-terre-battue-975-75", ("#fef4f2", "#281a16"), ("#fcd8d0", "#513932"), ("#fac5b8", "#6a4b42")),
        ("orange-terre-battue-950-100", ("#fee9e5", "#31201c"), ("#fdc6ba", "#5d403a"), ("#fcb09e", "#77534a")),
        ("orange-terre-battue-925-125", ("#fddfd8", "#382621"), ("#fbb8a5", "#664840"), ("#faa184", "#7f5b51")),
        ("orange-terre-battue-850-200", ("#fcc0b0", "#543125"), None, None),
    ],
    "Café crème {scheme_label}": [
        ("brown-cafe-creme-main-782", ("#d1b781", "#d1b781"), None, None),
        ("brown-cafe-creme-sun-383-moon-885", ("#685c48", "#ecd7a2"), ("#97866a", "#c5b386"), ("#ae9b7b", "#af9f77")),
        ("brown-cafe-creme-975-75", ("#fbf6ed", "#211d16"), ("#f2deb6", "#453e31"), ("#eacf91", "#5a5141")),
        ("brown-cafe-creme-950-100", ("#f7ecdb", "#28241c"), ("#edce94", "#4e4739"), ("#dabd84", "#635b4a")),
        ("brown-cafe-creme-925-125", ("#f4e3c7", "#2e2a21"), ("#e1c386", "#554e3f"), ("#ccb078", "#6b6351")),
        ("brown-cafe-creme-850-200", ("#e7ca8e", "#423925"), None, None),
    ],
    "Caramel {scheme_label}": [
        ("brown-caramel-main-648", ("#c08c65", "#c08c65"), None, None),
        ("brown-caramel-sun-425-moon-901", ("#845d48", "#fbd8ab"), ("#bb8568", "#efb547"), ("#d69978", "#d6a23e")),
        ("brown-caramel-975-75", ("#fbf5f2", "#251c16"), ("#f1dbcf", "#4c3c31"), ("#ecc9b5", "#624e41")),
        ("brown-caramel-950-100", ("#f7ebe5", "#2c221c"), ("#eccbb9", "#554439"), ("#e6b79a", "#6c574a")),
        ("brown-caramel-925-125", ("#f3e2d9", "#332821"), ("#e7bea6", "#5d4b40"), ("#e1a982", "#755f51")),
        ("brown-caramel-850-200", ("#eac7b2", "#4b3525"), None, None),
    ],
    "Opéra {scheme_label}": [
        ("brown-opera-main-680", ("#bd987a", "#bd987a"), None, None),
        ("brown-opera-sun-395-moon-820", ("#745b47", "#e6be92"), ("#a78468", "#f2e2d3"), ("#c09979", "#f8f0e9")),
        ("brown-opera-975-75", ("#fbf5f2", "#241c17"), ("#f1dbcf", "#4a3c33"), ("#ecc9b5", "#604f44")),
        ("brown-opera-950-100", ("#f7ece4", "#2b221c"), ("#eccdb3", "#53443a"), ("#e6ba90", "#6a574a")),
        ("brown-opera-925-125", ("#f3e2d7", "#322821"), ("#e7bfa0", "#5c4b40"), ("#deaa7e", "#735f51")),
        ("brown-opera-850-200", ("#eac7ad", "#493625"), None, None),
    ],
    "Gris galet {scheme_label}": [
        ("beige-gris-galet-main-702", ("#aea397", "#aea397"), None, None),
        ("beige-gris-galet-sun-407-moon-821", ("#6a6156", "#d0c3b7"), ("#988b7c", "#eae5e1"), ("#afa08f", "#f4f2f0")),
        ("beige-gris-galet-975-75", ("#f9f6f2", "#211d19"), ("#eadecd", "#453e37"), ("#e1ceb1", "#595148")),
        ("beige-gris-galet-950-100", ("#f3ede5", "#28231f"), ("#e1d0b5", "#4e453f"), ("#d1bea2", "#635950")),
        ("beige-gris-galet-925-125", ("#eee4d9", "#2e2924"), ("#dbc3a4", "#554d45"), ("#c6b094", "#6b6157")),
        ("beige-gris-galet-850-200", ("#e0cab0", "#433829"), None, None),
    ],
}

# Decision tokens — mirrors the canonical DSFR documentation page
# (https://www.systeme-de-design.gouv.fr/version-courante/fr/fondamentaux/couleurs-palette).
# Three sections, 30 user-facing tokens with usage descriptions and
# concrete examples. Each row points at a paired option token whose
# (light, dark) values are looked up in PALETTE for swatch rendering.
#
# Format per row: (token, paired_option, description, example).
DECISION_SECTIONS = [
    ("Couleurs de fond", [
        ("background-alt-grey", "grey-975-75",
         "Fond de blocs ou de sections",
         "Pied de page"),
        ("background-alt-blue-france", "blue-france-975-75",
         "Fond de bloc de page aux couleurs de l'État",
         "Lettre d'information et réseaux sociaux"),
        ("background-contrast-grey", "grey-950-100",
         "Fond de composant contrastant",
         "Mise en avant, champ de saisie"),
        ("background-elevated-grey", "grey-1000-75",
         "Fond de composant en relief",
         "En-tête, menu déroulant"),
        ("background-action-high-blue-france", "blue-france-sun-113-625",
         "Fond de composant cliquable important et portant l'identité de l'État",
         "Bouton primaire"),
        ("background-action-low-blue-france", "blue-france-925-125",
         "Fond de composant cliquable mineur et portant l'identité de l'État",
         "Tag cliquable"),
        ("background-active-blue-france", "blue-france-sun-113-625",
         "Fond de composant actif et portant l'identité de l'État",
         "Pagination"),
        ("background-open-blue-france", "blue-france-925-125",
         "Fond de composant ouvert et portant l'identité de l'État",
         "Élément de navigation"),
        ("background-disabled-grey", "grey-925-125",
         "Fond de composant désactivé",
         "Boutons, tag"),
        ("background-flat-error", "error-425-625",
         "Fond de composant en état d'erreur",
         "Alerte"),
        ("background-flat-warning", "warning-425-625",
         "Fond de composant en état d'avertissement",
         "Alerte"),
        ("background-flat-success", "success-425-625",
         "Fond de composant en état de succès",
         "Alerte"),
        ("background-flat-info", "info-425-625",
         "Fond de composant en état d'information",
         "Alerte"),
        ("background-default-grey", "grey-1000-50",
         "Fonds de page et de composant par défaut",
         "Pied de page, modale, onglet"),
    ]),
    ("Couleurs de texte", [
        ("text-title-grey", "grey-50-1000",
         "Titre ou élément équivalent",
         "Titres éditoriaux, titre de tableau"),
        ("text-title-blue-france", "blue-france-sun-113-625",
         "Titre portant l'identité de l'État",
         "—"),
        ("text-default-grey", "grey-200-850",
         "Corps de texte",
         "—"),
        ("text-mention-grey", "grey-425-625",
         "Texte de mentions ou de détail",
         "—"),
        ("text-label-grey", "grey-50-1000",
         "Texte de libellé",
         "Éléments de formulaire"),
        ("text-action-high-blue-france", "blue-france-sun-113-625",
         "Texte cliquable important et portant l'identité de l'État",
         "Bouton secondaire"),
        ("text-action-high-grey", "grey-50-1000",
         "Texte cliquable important",
         "Accordéon, élément de navigation"),
        ("text-inverted-grey", "grey-1000-50",
         "Texte ou icône contrastant en nuances de gris",
         "Alerte"),
        ("text-inverted-blue-france", "blue-france-975-sun-113",
         "Texte ou icône contrastant portant l'identité de l'État",
         "Bouton primaire, pagination, tag"),
        ("text-active-blue-france", "blue-france-sun-113-625",
         "Texte actif portant l'identité de l'État",
         "Élément de navigation, interrupteur"),
        ("text-active-grey", "grey-50-1000",
         "Texte actif neutre",
         "Fil d'Ariane"),
        ("text-disabled-grey", "grey-625-425",
         "Texte désactivé",
         "—"),
        ("text-default-error", "error-425-625",
         "Texte ou icône en état d'erreur",
         "Champ de saisie, élément de formulaire"),
        ("text-default-success", "success-425-625",
         "Texte ou icône en état de succès",
         "Champ de saisie, élément de formulaire"),
    ]),
    ("Couleurs d'illustrations", [
        ("artwork-major-blue-france", "blue-france-sun-113-625",
         "Couleur dominante d'illustration (60%)",
         "Illustration des options de paramètres d'affichage"),
        ("artwork-minor-blue-france", "blue-france-main-525",
         "Icône portant l'identité de l'État ou couleur mineure d'illustration (30%)",
         "Citation"),
    ]),
]

# Known token-name family prefixes for paired-option decomposition.
# Order matters: longer prefixes must come before shorter ones so that
# `blue-france` is matched before `blue` (which isn't a family).
DSFR_FAMILIES = (
    "blue-france", "red-marianne",
    "info", "success", "warning", "error",
    "grey",
)


def decompose_paired(paired: str) -> tuple[str, str]:
    """Split a paired option token like `grey-975-75` into the two
    single-theme reference labels the DSFR docs print: ("grey-975", "grey-75").

    Recognised forms (after stripping the family prefix):
        main-XXX        theme-stable; both labels equal the full name.
        N-N             two numeric segments → ("<fam>-<L>", "<fam>-<D>")
        sun-N-N         three segments       → ("<fam>-sun-<L>", "<fam>-<D>")
        N-sun-N         three segments       → ("<fam>-<L>", "<fam>-sun-<D>")

    Anything else (illustrative `sun-X-moon-Y` etc.) is returned as-is
    in both slots since the DSFR docs only use this for the seven
    canonical decision-token families above.
    """
    fam = next((f for f in DSFR_FAMILIES if paired.startswith(f + "-")), None)
    if not fam:
        return paired, paired
    suffix = paired[len(fam) + 1:]
    if suffix.startswith("main-"):
        return paired, paired
    parts = suffix.split("-")
    if len(parts) == 2 and all(p.isdigit() for p in parts):
        return f"{fam}-{parts[0]}", f"{fam}-{parts[1]}"
    if len(parts) == 3 and parts[0] == "sun":
        return f"{fam}-sun-{parts[1]}", f"{fam}-{parts[2]}"
    if len(parts) == 3 and parts[1] == "sun":
        return f"{fam}-{parts[0]}", f"{fam}-sun-{parts[2]}"
    return paired, paired


# Flat hex lookup populated from PALETTE: token-name → (light_hex, dark_hex).
PALETTE_HEX: dict[str, tuple[str, str]] = {
    tok: default
    for shades in PALETTE.values()
    for tok, default, _hover, _active in shades
}


# ---------------------------------------------------------------------
# Generators
# ---------------------------------------------------------------------

# Typography — mirrors the canonical DSFR documentation page
# (https://www.systeme-de-design.gouv.fr/version-courante/fr/fondamentaux/typographie).
# Two sections: Titres (semantic h1-h6) and Titres alternatifs
# (display-only `fr-display--*` classes). Each row carries usage
# description, the HTML balise / CSS class binding, and BOTH
# desktop + mobile attributes. Sample text is rendered live with
# the row's actual font size to make scale comparisons obvious.
#
# Format per row: (level, sample, usage, balise_or_class,
#                  (desktop_size, desktop_lh, desktop_mb),
#                  (mobile_size,  mobile_lh,  mobile_mb))
# Sizes/lh in px (the docs print px, not rem); margin-bottom is
# fixed per section (24px titles, 32px displays) but kept on each
# row for symmetry with the docs.
TITRES = [
    ("H1",
     "République numérique",
     "Titre principal de la page : il ne peut y en avoir qu'un par page.",
     "&lt;h1&gt;",
     (40, 48, 24), (32, 40, 24)),
    ("H2",
     "Démarches en ligne",
     "Second niveau de titre de section ou de paragraphes. Leur nombre n'est pas limité.",
     "&lt;h2&gt;",
     (32, 40, 24), (28, 36, 24)),
    ("H3",
     "Vos services administratifs",
     "Troisième niveau de sous-titre. Leur nombre n'est pas limité.",
     "&lt;h3&gt;",
     (28, 36, 24), (24, 32, 24)),
    ("H4",
     "Informations pratiques",
     "Quatrième niveau de sous-titre. Leur nombre n'est pas limité.",
     "&lt;h4&gt;",
     (24, 32, 24), (22, 28, 24)),
    ("H5",
     "Sous-titre de section",
     "Cinquième niveau de sous-titre. Leur nombre n'est pas limité.",
     "&lt;h5&gt;",
     (22, 28, 24), (20, 28, 24)),
    ("H6",
     "Intertitre minimal",
     "Sixième et plus petit niveau de sous-titre. Leur nombre n'est pas limité.",
     "&lt;h6&gt;",
     (20, 28, 24), (18, 24, 24)),
]

TITRES_ALTERNATIFS = [
    ("Titre alternatif XL", "République", "fr-display--xl", (80, 88, 32), (72, 80, 32)),
    ("Titre alternatif LG", "République", "fr-display--lg", (72, 80, 32), (64, 72, 32)),
    ("Titre alternatif MD", "République", "fr-display--md", (64, 72, 32), (56, 64, 32)),
    ("Titre alternatif SM", "République", "fr-display--sm", (56, 64, 32), (48, 56, 32)),
    ("Titre alternatif XS", "République", "fr-display--xs", (48, 56, 32), (40, 48, 32)),
]

# Body / lead / label / Spectral — size-stable across breakpoints
# (no @media overrides in the canonical CSS), so a single column
# of attributes is sufficient.
# Format: (token, sample, usage, classe, size_px, lh_px, weight, font_label)
CORPS_DE_TEXTE = [
    ("body-xl",
     "Le DSFR garantit la cohérence visuelle des sites de l'État.",
     "Paragraphe d'accroche (lead) en tête d'article ou de section.",
     "fr-text--xl / fr-text--lead", 20, 32, 400, "Marianne"),
    ("body-lg",
     "Le DSFR garantit la cohérence visuelle des sites de l'État et améliore l'expérience des usagers.",
     "Paragraphe mis en avant ou texte courant légèrement agrandi.",
     "fr-text--lg", 18, 28, 400, "Marianne"),
    ("body-md",
     "Texte courant des services publics numériques. Lisibilité prioritaire, hauteur de ligne 24px.",
     "Corps de texte par défaut.",
     "fr-text--md", 16, 24, 400, "Marianne"),
    ("body-sm",
     "Métadonnées et texte secondaire — date de mise à jour, légendes, mentions.",
     "Texte secondaire ou métadonnées.",
     "fr-text--sm", 14, 24, 400, "Marianne"),
    ("body-xs",
     "Microcopie, légendes de tableau, indications techniques.",
     "Microcopie : légendes de tableau, indications techniques.",
     "fr-text--xs", 12, 20, 400, "Marianne"),
    ("label",
     "Libellé de champ ou de bouton",
     "Libellés de formulaires, textes de boutons.",
     "—", 14, 24, 700, "Marianne"),
    ("body-md-alt",
     "Variante éditoriale pour distinguer un passage : citation, exergue, encadré littéraire.",
     "Variante éditoriale serif (Spectral).",
     "fr-text--alt + fr-text--md", 16, 24, 400, "Spectral"),
    ("body-sm-alt",
     "Note de bas de page ou source en serif.",
     "Note de bas de page ou source en serif.",
     "fr-text--alt + fr-text--sm", 14, 24, 400, "Spectral"),
]


def scheme_label(scheme: str) -> str:
    """French label suffix matching the DSFR doc captures."""
    return "(thème clair)" if scheme == "light" else "(thème sombre)"


def format_group_name(group_name: str, scheme: str) -> str:
    """Substitute the `{scheme_label}` placeholder in a PALETTE key.

    Groups whose title varies by theme (the four system families:
    Info, Succès, Avertissement, Erreur) include `{scheme_label}` in
    their key. Groups whose title is theme-stable pass through
    unchanged.
    """
    return group_name.format(scheme_label=scheme_label(scheme))


def css_var_block(scheme: str) -> str:
    """Emit the :root { --c-... } block with all option tokens flattened."""
    idx = 0 if scheme == "light" else 1
    lines: list[str] = []
    for group_name, shades in PALETTE.items():
        lines.append(f"      /* ---- {format_group_name(group_name, scheme)} ---- */")
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
        title = format_group_name(group_name, scheme)
        # The first illustrative family (Tilleul verveine) gets a one-time
        # intro paragraph that applies to all 17 families that follow.
        if group_name.startswith("Tilleul verveine"):
            out.append('    <h2 style="margin-top:3rem;">Accents illustratifs · une famille par page</h2>')
            out.append('    <p class="muted" style="font-size:0.875rem;">')
            out.append('      17 familles, réservées à l\'éditorial. Jamais utilisées pour les actions ou les couleurs système.')
            out.append('      Chaque famille expose 6 nuances (main → sun-moon → 975 → 950 → 925 → 850).')
            out.append('    </p>')
        out.append(f'    <div class="group-label">{title}</div>')
        out.append('    <div class="shade-grid">')
        for token, default, hover, active in shades:
            out.append('      ' + shade_card(token, default, hover, active, scheme))
        out.append('    </div>')
        out.append('')
    return "\n".join(out)


def decision_table_html(scheme: str) -> str:
    """Render the three DSFR decision-token tables (Fond, Texte, Illustrations).

    Each preview file is theme-specific (preview.html vs
    preview-dark.html) and the colour swatches elsewhere on the page
    reflect that single theme — so the decision-tokens table follows
    the same convention and shows only the column relevant to the
    file's scheme. `scheme="light"` emits a "Thème clair" column;
    `scheme="dark"` emits a "Thème sombre" column.
    """
    idx = 0 if scheme == "light" else 1
    column_title = "Thème clair" if scheme == "light" else "Thème sombre"
    out: list[str] = []
    out.append('    <h3>Tokens de décision</h3>')
    out.append('    <p>Les composants doivent référencer ces tokens, pas les options brutes.')
    out.append('       Chaque token de décision pointe vers un token d\'option différent selon le thème (clair / sombre).</p>')
    for section_title, rows in DECISION_SECTIONS:
        out.append(f'    <h4 style="margin-top:2rem;">{section_title}</h4>')
        out.append('    <table class="tokens decisions">')
        out.append('      <thead>')
        out.append('        <tr>')
        out.append('          <th>Description de l\'usage</th>')
        out.append('          <th>Token</th>')
        out.append(f'          <th>{column_title}</th>')
        out.append('        </tr>')
        out.append('      </thead>')
        out.append('      <tbody>')
        for tok, paired, desc, example in rows:
            light_ref, dark_ref = decompose_paired(paired)
            theme_ref = light_ref if scheme == "light" else dark_ref
            theme_hex = PALETTE_HEX.get(paired, ("?", "?"))[idx]
            example_html = (
                f'<br><span class="muted" style="font-size:0.875rem;">Exemple : {example}</span>'
                if example and example != "—" else ""
            )
            out.append(
                f'        <tr>'
                f'<td>{desc}{example_html}</td>'
                f'<td class="tok">${tok}</td>'
                f'<td class="tok">'
                f'<span class="dot" style="background:{theme_hex}"></span>'
                f'${theme_ref} <span class="muted">({theme_hex})</span>'
                f'</td>'
                f'</tr>'
            )
        out.append('      </tbody>')
        out.append('    </table>')
    return "\n".join(out)


def _attr_cell(size_px: int, lh_px: int, mb_px: int) -> str:
    """Render a 'Taille / Line-height / Margin-bottom' cell as the
    DSFR docs do — three short labelled lines stacked vertically."""
    return (
        f'Taille&nbsp;: {size_px} px<br>'
        f'Line-height&nbsp;: {lh_px} px<br>'
        f'Margin-bottom&nbsp;: {mb_px} px'
    )


def _sample_style(size_px: int, lh_px: int, weight: int = 700,
                  font: str = "Marianne") -> str:
    """Inline `style=` for a live-rendered sample cell. Uses the
    actual font-size/line-height so visual scale matches the row's
    declared attributes (DSFR docs use a generic Aa; we do better
    by rendering the row's own sample text at full size)."""
    var_font = "var(--font-marianne)" if font == "Marianne" else "var(--font-spectral)"
    # Cap the sample size so massive XL/LG displays don't blow out
    # the table layout. The DSFR docs use a fixed-size "Aa" placeholder
    # for the same reason; we stick with the row's font but limit the
    # rendered size to a reasonable preview ceiling.
    rendered_size = min(size_px, 56)
    rendered_lh = lh_px if size_px <= 56 else int(lh_px * (rendered_size / size_px))
    return (
        f'font: {weight} {rendered_size}px/{rendered_lh}px {var_font};'
        f' color: var(--c-text-default-grey);'
        f' white-space: nowrap;'
        f' overflow: hidden;'
        f' text-overflow: ellipsis;'
    )


def typography_section_html() -> str:
    """Render the three DSFR typography tables.

    Section 1: Titres — semantic h1-h6, 6-column layout matching the
        DSFR docs (Niveau / Aperçu / Usages / Balise / Desktop / Mobile).

    Section 2: Titres alternatifs — display sizes (`fr-display--*`),
        same shape but with a "Classe" column instead of "Balise".

    Section 3: Corps de texte — body / lead / label / Spectral.
        Body sizes are size-stable across breakpoints, so a single
        attributes column suffices.

    Output is the same in both preview files (typography is theme-stable).
    """
    out: list[str] = []
    out.append('    <h2>Typographie</h2>')
    out.append('    <p class="lede">Marianne est la fonte principale (sans-serif, dessinée pour l\'État&nbsp;; '
               'weights 300/400/500/700). Spectral est la fonte secondaire (serif, 400/800), '
               'réservée aux passages distinctifs ou éditoriaux via la classe '
               '<code>fr-text--alt</code>.</p>')

    # ---- Section 1: Titres ----
    out.append('    <h3 style="margin-top:2rem;">Titres</h3>')
    out.append('    <p>Les niveaux <code>h1</code>–<code>h6</code> sont rendus par les balises HTML '
               'natives ou par la classe utilitaire <code>fr-h1</code>…<code>fr-h6</code>. '
               'La taille bascule automatiquement sur le palier mobile au-dessous de '
               '<code>48em</code> (768&nbsp;px). Couleur&nbsp;: '
               '<code>text-title-grey</code> sur fond clair, blanc sur fond sombre.</p>')
    out.append('    <table class="tokens typography">')
    out.append('      <thead>')
    out.append('        <tr>')
    out.append('          <th style="width:8rem;">Niveau</th>')
    out.append('          <th>Aperçu</th>')
    out.append('          <th>Usages</th>')
    out.append('          <th style="width:6rem;">Balise</th>')
    out.append('          <th style="width:11rem;">Attributs desktop</th>')
    out.append('          <th style="width:11rem;">Attributs mobile</th>')
    out.append('        </tr>')
    out.append('      </thead>')
    out.append('      <tbody>')
    for level, sample, usage, balise, desktop, mobile in TITRES:
        out.append(
            f'        <tr>'
            f'<td><strong>{level}</strong></td>'
            f'<td><span style="{_sample_style(*desktop[:2])}">{sample}</span></td>'
            f'<td>{usage}</td>'
            f'<td class="tok">{balise}</td>'
            f'<td>{_attr_cell(*desktop)}</td>'
            f'<td>{_attr_cell(*mobile)}</td>'
            f'</tr>'
        )
    out.append('      </tbody>')
    out.append('    </table>')

    # ---- Section 2: Titres alternatifs ----
    out.append('    <h3 style="margin-top:2.5rem;">Titres alternatifs</h3>')
    out.append('    <p>Cinq tailles de titres oversize pour usages éditoriaux ou marketing. '
               'Non sémantiques&nbsp;: à appliquer via la classe utilitaire '
               '<code>fr-display--{size}</code> sur l\'élément de titre approprié '
               '(le plus souvent <code>&lt;h1&gt;</code>). Couleur identique aux titres&nbsp;; '
               'margin-bottom&nbsp;: 32&nbsp;px.</p>')
    out.append('    <table class="tokens typography">')
    out.append('      <thead>')
    out.append('        <tr>')
    out.append('          <th style="width:11rem;">Niveau</th>')
    out.append('          <th>Aperçu</th>')
    out.append('          <th style="width:9rem;">Classe</th>')
    out.append('          <th style="width:11rem;">Attributs desktop</th>')
    out.append('          <th style="width:11rem;">Attributs mobile</th>')
    out.append('        </tr>')
    out.append('      </thead>')
    out.append('      <tbody>')
    for level, sample, classe, desktop, mobile in TITRES_ALTERNATIFS:
        out.append(
            f'        <tr>'
            f'<td><strong>{level}</strong></td>'
            f'<td><span style="{_sample_style(*desktop[:2])}">{sample}</span></td>'
            f'<td class="tok">{classe}</td>'
            f'<td>{_attr_cell(*desktop)}</td>'
            f'<td>{_attr_cell(*mobile)}</td>'
            f'</tr>'
        )
    out.append('      </tbody>')
    out.append('    </table>')

    # ---- Section 3: Corps de texte ----
    out.append('    <h3 style="margin-top:2.5rem;">Corps de texte</h3>')
    out.append('    <p>Tailles stables sur tous les paliers (pas de surcharge mobile). '
               'Les variantes <em>-alt</em> en Spectral s\'obtiennent en combinant '
               '<code>fr-text--alt</code> avec la classe de taille.</p>')
    out.append('    <table class="tokens typography">')
    out.append('      <thead>')
    out.append('        <tr>')
    out.append('          <th style="width:8rem;">Token</th>')
    out.append('          <th>Aperçu</th>')
    out.append('          <th>Usages</th>')
    out.append('          <th style="width:13rem;">Classe</th>')
    out.append('          <th style="width:11rem;">Attributs</th>')
    out.append('        </tr>')
    out.append('      </thead>')
    out.append('      <tbody>')
    for token, sample, usage, classe, size, lh, weight, font in CORPS_DE_TEXTE:
        attr = (
            f'Taille&nbsp;: {size} px<br>'
            f'Line-height&nbsp;: {lh} px<br>'
            f'Weight&nbsp;: {weight}<br>'
            f'Fonte&nbsp;: {font}'
        )
        out.append(
            f'        <tr>'
            f'<td class="tok">${token}</td>'
            f'<td><span style="{_sample_style(size, lh, weight, font)}">{sample}</span></td>'
            f'<td>{usage}</td>'
            f'<td class="tok">{classe}</td>'
            f'<td>{attr}</td>'
            f'</tr>'
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

    # 4. Replace the typography section (theme-stable; same body
    #    in both preview files).
    typo = typography_section_html()
    src = replace_block(
        src,
        "<!-- BEGIN GENERATED TYPOGRAPHY -->",
        "<!-- END GENERATED TYPOGRAPHY -->",
        typo,
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
