---
version: alpha
name: DSFR — Système de Design de l'État
description: >
  Design tokens and component patterns derived from the official French
  government design system (DSFR v1.14, https://www.systeme-de-design.gouv.fr).
  Encodes the Bleu France / Rouge Marianne brand identity, Marianne & Spectral
  typography, the v-based spacing scale, and core component decision tokens
  for the LIGHT theme. Components follow BEM (`fr-*` classes) and target
  RGAA / WCAG 2.1 AA compliance. Dark-theme mappings are documented in prose.

colors:
  # ============================================================
  # OPTION TOKENS — raw palette, indexed by hue/family
  # ============================================================
  # These mirror the DSFR token names of the form
  #   COULEUR-NOM-VARIANTE-INDICE-ÉTAT
  # so they can be grepped against the official documentation.

  # ---------- Brand: Bleu France ----------
  blue-france-sun-113-625:        "#000091"
  blue-france-sun-113-625-hover:  "#1212ff"
  blue-france-sun-113-625-active: "#2323ff"
  blue-france-main-525:           "#6a6af4"
  blue-france-850-200:            "#cacafb"
  blue-france-925-125:            "#e3e3fd"
  blue-france-925-125-hover:      "#c1c1fb"
  blue-france-925-125-active:     "#adadf9"
  blue-france-950-100:            "#ececfe"
  blue-france-950-100-hover:      "#cecefc"
  blue-france-950-100-active:     "#bbbbfc"
  blue-france-975-75:             "#f5f5fe"
  blue-france-975-75-hover:       "#dcdcfc"
  blue-france-975-75-active:      "#cbcbfa"

  # ---------- Brand: Rouge Marianne ----------
  red-marianne-425-625:           "#c9191e"
  red-marianne-425-625-hover:     "#f93f42"
  red-marianne-425-625-active:    "#f95a5c"
  red-marianne-main-472:          "#e1000f"
  red-marianne-850-200:           "#fcbfbf"
  red-marianne-925-125:           "#fddede"
  red-marianne-925-125-hover:     "#fbb6b6"
  red-marianne-925-125-active:    "#fa9e9e"
  red-marianne-950-100:           "#fee9e9"
  red-marianne-950-100-hover:     "#fdc5c5"
  red-marianne-950-100-active:    "#fcafaf"
  red-marianne-975-75:            "#fef4f4"
  red-marianne-975-75-hover:      "#fcd7d7"
  red-marianne-975-75-active:     "#fac4c4"
  # Special pairing: light=blue-france-975 (pale tint), dark=blue-france-sun-113
  # (saturated brand blue). Used by `text-inverted-blue-france` so that
  # "inverted" text on a Bleu France background remains the brand blue
  # in dark mode (rather than flipping to white).
  blue-france-975-sun-113:        "#f5f5fe"

  # ---------- Neutrals (greys) — light-theme orientation ----------
  # As with the brand colours, the DSFR ships hover/active states only
  # for the grey shades intended as interactive surfaces (white surface,
  # tinted backgrounds, action-text). Borders, body text, mention text,
  # absolute black/white and the docs-only `main` and `850-200` shades
  # are static — they have no hover/active in the canonical CSS.
  grey-main-525:                  "#7b7b7b"
  grey-1000-50:                   "#ffffff"
  grey-1000-50-hover:             "#f6f6f6"
  grey-1000-50-active:            "#ededed"
  grey-975-100:                   "#f6f6f6"
  grey-975-100-hover:             "#dfdfdf"
  grey-975-100-active:            "#cfcfcf"
  # Canonical decision-token target for `background-alt-grey`.
  grey-975-75:                    "#f6f6f6"
  grey-975-75-hover:              "#dfdfdf"
  grey-975-75-active:             "#cfcfcf"
  # Canonical decision-token target for `background-raised-grey`
  # and `background-lifted-grey` — used by `.fr-card--shadow`
  # and elevated callouts. Identical to grey-1000-50 in light
  # theme but distinct in dark (#1e1e1e vs #161616).
  grey-1000-75:                   "#ffffff"
  grey-1000-75-hover:             "#f6f6f6"
  grey-1000-75-active:            "#ededed"
  grey-950-150:                   "#eeeeee"
  grey-950-150-hover:             "#d2d2d2"
  grey-950-150-active:            "#c1c1c1"
  # Canonical decision-token target for `background-contrast-grey`.
  grey-950-100:                   "#eeeeee"
  grey-950-100-hover:             "#d2d2d2"
  grey-950-100-active:            "#c1c1c1"
  # Canonical decision-token target for
  # `background-contrast-raised-grey` — used when both
  # `--shadow` and `--grey` modifiers stack on a card.
  grey-950-125:                   "#eeeeee"
  grey-950-125-hover:             "#d2d2d2"
  grey-950-125-active:            "#c1c1c1"
  grey-925-125:                   "#e5e5e5"
  grey-900-175:                   "#dddddd"
  grey-850-200:                   "#cecece"
  grey-625-425:                   "#929292"
  grey-425-625:                   "#666666"
  grey-200-850:                   "#3a3a3a"
  grey-200-850-hover:             "#616161"
  grey-200-850-active:            "#777777"
  grey-50-1000:                   "#161616"
  grey-0-1000:                    "#000000"

  # ---------- System (functional) ----------
  # Family order matches the DSFR documentation captures:
  # info → succès → avertissement → erreur.
  #
  # Each family exposes 6 shades following the same convention as the
  # brand colours (main → strong → lightest → lighter → light → softest):
  #   - `-main-525` reference value (theme-stable, both themes use the
  #                 same hex). Documented in DSFR but NOT exposed as a
  #                 CSS variable in `dsfr.css`. Same category as
  #                 `blue-france-main-525`, `grey-main-525`, etc.
  #   - `-425-625`  strong / saturated. Solid status backgrounds, and
  #                 also the canonical text-default-* color (DSFR
  #                 aliases text-default-success → success-425-625, etc.)
  #   - `-975-75`   lightest / alert background tint
  #   - `-950-100`  lighter / low-emphasis status surfaces
  #   - `-925-125`  light / docs-only reference (NOT in `dsfr.css`)
  #   - `-850-200`  softest / docs-only reference (NOT in `dsfr.css`)
  # Only `-425-625`, `-950-100`, and `-975-75` are compiled into the
  # canonical CSS distribution; the other three are reference values
  # listed in the DSFR's palette page for design-time use.
  # All four families pass WCAG AA at body text size on their `-975-75`
  # alert background using their `-425-625` for text.
  info-main-525:                  "#0078f3"
  info-425-625:                   "#0063cb"
  info-425-625-hover:             "#3b87ff"
  info-425-625-active:            "#6798ff"
  info-975-75:                    "#f4f6ff"
  info-950-100:                   "#e8edff"
  info-950-100-hover:             "#c2d1ff"
  info-950-100-active:            "#a9bfff"
  info-925-125:                   "#dde5ff"
  info-850-200:                   "#bccdff"
  success-main-525:               "#1f8d49"
  success-425-625:                "#18753c"
  success-425-625-hover:          "#27a959"
  success-425-625-active:         "#2fc368"
  success-975-75:                 "#dffee6"
  success-950-100:                "#b8fec9"
  success-950-100-hover:          "#46fd89"
  success-950-100-active:         "#34eb7b"
  success-925-125:                "#88fdaa"
  success-850-200:                "#3bea7e"
  warning-main-525:               "#d64d00"
  warning-425-625:                "#b34000"
  warning-425-625-hover:          "#ff6218"
  warning-425-625-active:         "#ff7a55"
  warning-975-75:                 "#fff4f3"
  warning-950-100:                "#ffe9e6"
  warning-950-100-hover:          "#ffc6bd"
  warning-950-100-active:         "#ffb0a2"
  warning-925-125:                "#ffded9"
  warning-850-200:                "#ffbeb4"
  error-main-525:                 "#f60700"
  error-425-625:                  "#ce0500"
  error-425-625-hover:            "#ff2725"
  error-425-625-active:           "#ff4140"
  error-975-75:                   "#fff4f4"
  error-950-100:                  "#ffe9e9"
  error-950-100-hover:            "#ffc5c5"
  error-950-100-active:           "#ffafaf"
  error-925-125:                  "#ffdddd"
  error-850-200:                  "#ffbdbd"

  # ---------- Illustrative accents (17 families) ----------
  # Family order matches the DSFR documentation captures:
  # tilleul-verveine → bourgeon → émeraude → menthe → archipel → écume →
  # cumulus → glycine → macaron → tuile → tournesol → moutarde →
  # terre-battue → café-crème → caramel → opéra → gris-galet.
  #
  # Each family exposes 6 shades (same convention as system colours):
  #   - `-main-XXX`             reference value (theme-stable, docs-only,
  #                             NOT exposed as a CSS variable). XXX is
  #                             the family-specific main level.
  #   - `-sun-XXX-moon-YYY`     strong / saturated. The "sun-XXX" segment
  #                             is the light-theme reference, "moon-YYY"
  #                             the dark-theme reference. Has hover/active.
  #   - `-975-75`               lightest / pale tint. Has hover/active.
  #   - `-950-100`              lighter. Has hover/active.
  #   - `-925-125`              light / docs-only reference. Has hover/active.
  #   - `-850-200`              softest / docs-only reference (no states).
  #
  # Most of these are intentionally orphaned at the YAML level: only the
  # main-XXX of each family appears in the canonical `border-default-*`
  # decision token (e.g. border-default-blue-cumulus references
  # blue-cumulus-main-526). The linter flags the remaining shades as
  # `orphaned-tokens`; this is desired — they're a richer vocabulary
  # available for editorial use, not a missing component reference.
  # ---- Tilleul verveine (green-tilleul-verveine) ----
  green-tilleul-verveine-main-707:                   "#b7a73f"
  green-tilleul-verveine-sun-418-moon-817:           "#66673d"
  green-tilleul-verveine-sun-418-moon-817-hover:     "#929359"
  green-tilleul-verveine-sun-418-moon-817-active:    "#a7a967"
  green-tilleul-verveine-975-75:                     "#fef7da"
  green-tilleul-verveine-975-75-hover:               "#fce552"
  green-tilleul-verveine-975-75-active:              "#ebd54c"
  green-tilleul-verveine-950-100:                    "#fceeac"
  green-tilleul-verveine-950-100-hover:              "#e8d45c"
  green-tilleul-verveine-950-100-active:             "#d4c254"
  green-tilleul-verveine-925-125:                    "#fbe769"
  green-tilleul-verveine-925-125-hover:              "#d7c655"
  green-tilleul-verveine-925-125-active:             "#c2b24c"
  green-tilleul-verveine-850-200:                    "#e2cf58"
  # ---- Bourgeon (green-bourgeon) ----
  green-bourgeon-main-640:                           "#68a532"
  green-bourgeon-sun-425-moon-759:                   "#447049"
  green-bourgeon-sun-425-moon-759-hover:             "#639f6a"
  green-bourgeon-sun-425-moon-759-active:            "#72b77a"
  green-bourgeon-975-75:                             "#e6feda"
  green-bourgeon-975-75-hover:                       "#a7fc62"
  green-bourgeon-975-75-active:                      "#98ed4d"
  green-bourgeon-950-100:                            "#c9fcac"
  green-bourgeon-950-100-hover:                      "#9ae95d"
  green-bourgeon-950-100-active:                     "#8dd555"
  green-bourgeon-925-125:                            "#a9fb68"
  green-bourgeon-925-125-hover:                      "#8ed654"
  green-bourgeon-925-125-active:                     "#7fc04b"
  green-bourgeon-850-200:                            "#95e257"
  # ---- Émeraude (green-emeraude) ----
  green-emeraude-main-632:                           "#00a95f"
  green-emeraude-sun-425-moon-753:                   "#297254"
  green-emeraude-sun-425-moon-753-hover:             "#3ea47a"
  green-emeraude-sun-425-moon-753-active:            "#49bc8d"
  green-emeraude-975-75:                             "#e3fdeb"
  green-emeraude-975-75-hover:                       "#94f9b9"
  green-emeraude-975-75-active:                      "#6df1a3"
  green-emeraude-950-100:                            "#c3fad5"
  green-emeraude-950-100-hover:                      "#77eda5"
  green-emeraude-950-100-active:                     "#6dd897"
  green-emeraude-925-125:                            "#9ef9be"
  green-emeraude-925-125-hover:                      "#69df97"
  green-emeraude-925-125-active:                     "#5ec988"
  green-emeraude-850-200:                            "#6fe49d"
  # ---- Menthe (green-menthe) ----
  green-menthe-main-548:                             "#009081"
  green-menthe-sun-373-moon-652:                     "#37635f"
  green-menthe-sun-373-moon-652-hover:               "#53918c"
  green-menthe-sun-373-moon-652-active:              "#62a9a2"
  green-menthe-975-75:                               "#dffdf7"
  green-menthe-975-75-hover:                         "#84f9e7"
  green-menthe-975-75-active:                        "#70ebd8"
  green-menthe-950-100:                              "#bafaee"
  green-menthe-950-100-hover:                        "#79e7d5"
  green-menthe-950-100-active:                       "#6fd3c3"
  green-menthe-925-125:                              "#8bf8e7"
  green-menthe-925-125-hover:                        "#6ed5c5"
  green-menthe-925-125-active:                       "#62bfb1"
  green-menthe-850-200:                              "#73e0cf"
  # ---- Archipel (green-archipel) ----
  green-archipel-main-557:                           "#009099"
  green-archipel-sun-391-moon-716:                   "#006a6f"
  green-archipel-sun-391-moon-716-hover:             "#009fa7"
  green-archipel-sun-391-moon-716-active:            "#00bbc3"
  green-archipel-975-75:                             "#e5fbfd"
  green-archipel-975-75-hover:                       "#99f2f8"
  green-archipel-975-75-active:                      "#73e9f0"
  green-archipel-950-100:                            "#c7f6fc"
  green-archipel-950-100-hover:                      "#64ecf8"
  green-archipel-950-100-active:                     "#5bd8e3"
  green-archipel-925-125:                            "#a6f2fa"
  green-archipel-925-125-hover:                      "#62dbe5"
  green-archipel-925-125-active:                     "#58c5cf"
  green-archipel-850-200:                            "#60e0eb"
  # ---- Écume (blue-ecume) ----
  blue-ecume-main-400:                               "#465f9d"
  blue-ecume-sun-247-moon-675:                       "#2f4077"
  blue-ecume-sun-247-moon-675-hover:                 "#4e68bb"
  blue-ecume-sun-247-moon-675-active:                "#667dcf"
  blue-ecume-975-75:                                 "#f4f6fe"
  blue-ecume-975-75-hover:                           "#d7dffb"
  blue-ecume-975-75-active:                          "#c3cffa"
  blue-ecume-950-100:                                "#e9edfe"
  blue-ecume-950-100-hover:                          "#c5d0fc"
  blue-ecume-950-100-active:                         "#adbffc"
  blue-ecume-925-125:                                "#dee5fd"
  blue-ecume-925-125-hover:                          "#b4c5fb"
  blue-ecume-925-125-active:                         "#99b3f9"
  blue-ecume-850-200:                                "#bfccfb"
  # ---- Cumulus (blue-cumulus) ----
  blue-cumulus-main-526:                             "#417dc4"
  blue-cumulus-sun-368-moon-732:                     "#3558a2"
  blue-cumulus-sun-368-moon-732-hover:               "#5982e0"
  blue-cumulus-sun-368-moon-732-active:              "#7996e6"
  blue-cumulus-975-75:                               "#f3f6fe"
  blue-cumulus-975-75-hover:                         "#d3dffc"
  blue-cumulus-975-75-active:                        "#bed0fa"
  blue-cumulus-950-100:                              "#e6eefe"
  blue-cumulus-950-100-hover:                        "#bcd3fc"
  blue-cumulus-950-100-active:                       "#9fc3fc"
  blue-cumulus-925-125:                              "#dae6fd"
  blue-cumulus-925-125-hover:                        "#a9c8fb"
  blue-cumulus-925-125-active:                       "#8ab8f9"
  blue-cumulus-850-200:                              "#b6cffb"
  # ---- Glycine (purple-glycine) ----
  purple-glycine-main-494:                           "#a558a0"
  purple-glycine-sun-319-moon-630:                   "#6e445a"
  purple-glycine-sun-319-moon-630-hover:             "#a66989"
  purple-glycine-sun-319-moon-630-active:            "#bb7f9e"
  purple-glycine-975-75:                             "#fef3fd"
  purple-glycine-975-75-hover:                       "#fcd4f8"
  purple-glycine-975-75-active:                      "#fabff5"
  purple-glycine-950-100:                            "#fee7fc"
  purple-glycine-950-100-hover:                      "#fdc0f8"
  purple-glycine-950-100-active:                     "#fca8f6"
  purple-glycine-925-125:                            "#fddbfa"
  purple-glycine-925-125-hover:                      "#fbaff5"
  purple-glycine-925-125-active:                     "#fa96f2"
  purple-glycine-850-200:                            "#fbb8f6"
  # ---- Macaron (pink-macaron) ----
  pink-macaron-main-689:                             "#e18b76"
  pink-macaron-sun-406-moon-833:                     "#8d533e"
  pink-macaron-sun-406-moon-833-hover:               "#ca795c"
  pink-macaron-sun-406-moon-833-active:              "#e08e73"
  pink-macaron-975-75:                               "#fef4f2"
  pink-macaron-975-75-hover:                         "#fcd8d0"
  pink-macaron-975-75-active:                        "#fac5b8"
  pink-macaron-950-100:                              "#fee9e6"
  pink-macaron-950-100-hover:                        "#fdc6bd"
  pink-macaron-950-100-active:                       "#fcb0a2"
  pink-macaron-925-125:                              "#fddfda"
  pink-macaron-925-125-hover:                        "#fbb8ab"
  pink-macaron-925-125-active:                       "#faa18d"
  pink-macaron-850-200:                              "#fcc0b4"
  # ---- Tuile (pink-tuile) ----
  pink-tuile-main-556:                               "#ce614a"
  pink-tuile-sun-425-moon-750:                       "#a94645"
  pink-tuile-sun-425-moon-750-hover:                 "#d5706f"
  pink-tuile-sun-425-moon-750-active:                "#da8a89"
  pink-tuile-975-75:                                 "#fef4f3"
  pink-tuile-975-75-hover:                           "#fcd7d3"
  pink-tuile-975-75-active:                          "#fac4be"
  pink-tuile-950-100:                                "#fee9e7"
  pink-tuile-950-100-hover:                          "#fdc6c0"
  pink-tuile-950-100-active:                         "#fcb0a7"
  pink-tuile-925-125:                                "#fddfdb"
  pink-tuile-925-125-hover:                          "#fbb8ad"
  pink-tuile-925-125-active:                         "#faa191"
  pink-tuile-850-200:                                "#fcbfb7"
  # ---- Tournesol (yellow-tournesol) ----
  yellow-tournesol-main-731:                         "#c8aa39"
  yellow-tournesol-sun-407-moon-922:                 "#716043"
  yellow-tournesol-sun-407-moon-922-hover:           "#a28a62"
  yellow-tournesol-sun-407-moon-922-active:          "#ba9f72"
  yellow-tournesol-975-75:                           "#fef6e3"
  yellow-tournesol-975-75-hover:                     "#fce086"
  yellow-tournesol-975-75-active:                    "#f5d24b"
  yellow-tournesol-950-100:                          "#feecc2"
  yellow-tournesol-950-100-hover:                    "#fbd335"
  yellow-tournesol-950-100-active:                   "#e6c130"
  yellow-tournesol-925-125:                          "#fde39c"
  yellow-tournesol-925-125-hover:                    "#e9c53b"
  yellow-tournesol-925-125-active:                   "#d3b235"
  yellow-tournesol-850-200:                          "#efcb3a"
  # ---- Moutarde (yellow-moutarde) ----
  yellow-moutarde-main-679:                          "#c3992a"
  yellow-moutarde-sun-348-moon-860:                  "#695240"
  yellow-moutarde-sun-348-moon-860-hover:            "#9b7b61"
  yellow-moutarde-sun-348-moon-860-active:           "#b58f72"
  yellow-moutarde-975-75:                            "#fef5e8"
  yellow-moutarde-975-75-hover:                      "#fcdca3"
  yellow-moutarde-975-75-active:                     "#fbcd64"
  yellow-moutarde-950-100:                           "#feebd0"
  yellow-moutarde-950-100-hover:                     "#fdcd6d"
  yellow-moutarde-950-100-active:                    "#f4be30"
  yellow-moutarde-925-125:                           "#fde2b5"
  yellow-moutarde-925-125-hover:                     "#f6c43c"
  yellow-moutarde-925-125-active:                    "#dfb135"
  yellow-moutarde-850-200:                           "#fcc63a"
  # ---- Terre battue (orange-terre-battue) ----
  orange-terre-battue-main-645:                      "#e4794a"
  orange-terre-battue-sun-370-moon-672:              "#755348"
  orange-terre-battue-sun-370-moon-672-hover:        "#ab7b6b"
  orange-terre-battue-sun-370-moon-672-active:       "#c68f7d"
  orange-terre-battue-975-75:                        "#fef4f2"
  orange-terre-battue-975-75-hover:                  "#fcd8d0"
  orange-terre-battue-975-75-active:                 "#fac5b8"
  orange-terre-battue-950-100:                       "#fee9e5"
  orange-terre-battue-950-100-hover:                 "#fdc6ba"
  orange-terre-battue-950-100-active:                "#fcb09e"
  orange-terre-battue-925-125:                       "#fddfd8"
  orange-terre-battue-925-125-hover:                 "#fbb8a5"
  orange-terre-battue-925-125-active:                "#faa184"
  orange-terre-battue-850-200:                       "#fcc0b0"
  # ---- Café crème (brown-cafe-creme) ----
  brown-cafe-creme-main-782:                         "#d1b781"
  brown-cafe-creme-sun-383-moon-885:                 "#685c48"
  brown-cafe-creme-sun-383-moon-885-hover:           "#97866a"
  brown-cafe-creme-sun-383-moon-885-active:          "#ae9b7b"
  brown-cafe-creme-975-75:                           "#fbf6ed"
  brown-cafe-creme-975-75-hover:                     "#f2deb6"
  brown-cafe-creme-975-75-active:                    "#eacf91"
  brown-cafe-creme-950-100:                          "#f7ecdb"
  brown-cafe-creme-950-100-hover:                    "#edce94"
  brown-cafe-creme-950-100-active:                   "#dabd84"
  brown-cafe-creme-925-125:                          "#f4e3c7"
  brown-cafe-creme-925-125-hover:                    "#e1c386"
  brown-cafe-creme-925-125-active:                   "#ccb078"
  brown-cafe-creme-850-200:                          "#e7ca8e"
  # ---- Caramel (brown-caramel) ----
  brown-caramel-main-648:                            "#c08c65"
  brown-caramel-sun-425-moon-901:                    "#845d48"
  brown-caramel-sun-425-moon-901-hover:              "#bb8568"
  brown-caramel-sun-425-moon-901-active:             "#d69978"
  brown-caramel-975-75:                              "#fbf5f2"
  brown-caramel-975-75-hover:                        "#f1dbcf"
  brown-caramel-975-75-active:                       "#ecc9b5"
  brown-caramel-950-100:                             "#f7ebe5"
  brown-caramel-950-100-hover:                       "#eccbb9"
  brown-caramel-950-100-active:                      "#e6b79a"
  brown-caramel-925-125:                             "#f3e2d9"
  brown-caramel-925-125-hover:                       "#e7bea6"
  brown-caramel-925-125-active:                      "#e1a982"
  brown-caramel-850-200:                             "#eac7b2"
  # ---- Opéra (brown-opera) ----
  brown-opera-main-680:                              "#bd987a"
  brown-opera-sun-395-moon-820:                      "#745b47"
  brown-opera-sun-395-moon-820-hover:                "#a78468"
  brown-opera-sun-395-moon-820-active:               "#c09979"
  brown-opera-975-75:                                "#fbf5f2"
  brown-opera-975-75-hover:                          "#f1dbcf"
  brown-opera-975-75-active:                         "#ecc9b5"
  brown-opera-950-100:                               "#f7ece4"
  brown-opera-950-100-hover:                         "#eccdb3"
  brown-opera-950-100-active:                        "#e6ba90"
  brown-opera-925-125:                               "#f3e2d7"
  brown-opera-925-125-hover:                         "#e7bfa0"
  brown-opera-925-125-active:                        "#deaa7e"
  brown-opera-850-200:                               "#eac7ad"
  # ---- Gris galet (beige-gris-galet) ----
  beige-gris-galet-main-702:                         "#aea397"
  beige-gris-galet-sun-407-moon-821:                 "#6a6156"
  beige-gris-galet-sun-407-moon-821-hover:           "#988b7c"
  beige-gris-galet-sun-407-moon-821-active:          "#afa08f"
  beige-gris-galet-975-75:                           "#f9f6f2"
  beige-gris-galet-975-75-hover:                     "#eadecd"
  beige-gris-galet-975-75-active:                    "#e1ceb1"
  beige-gris-galet-950-100:                          "#f3ede5"
  beige-gris-galet-950-100-hover:                    "#e1d0b5"
  beige-gris-galet-950-100-active:                   "#d1bea2"
  beige-gris-galet-925-125:                          "#eee4d9"
  beige-gris-galet-925-125-hover:                    "#dbc3a4"
  beige-gris-galet-925-125-active:                   "#c6b094"
  beige-gris-galet-850-200:                          "#e0cab0"

  # ============================================================
  # DECISION TOKENS — what components MUST reference
  # ============================================================
  # Naming convention: `<role>-<level>-<family>` (matches the DSFR's
  # canonical compiled CSS variable names exactly). Roles: background,
  # text, border, artwork. Common levels: default, alt, contrast,
  # action-high, action-low, active, plain, disabled, open, label,
  # title, mention, inverted. Families: grey (neutral), blue-france
  # (primary), the four system colours (info/success/warning/error),
  # and the 17 illustrative-accent families.
  #
  # Light/dark theme abstraction is automatic: each decision token
  # references a paired option token (e.g. `grey-1000-50`) whose two
  # values resolve through the consumer's theme system. We don't
  # duplicate decision tokens per theme.
  #
  # The block below is generated from canonical DSFR sources.
  # Don't edit by hand — re-run `python3 scripts/build-decisions.py`
  # and paste the output here.
  # ----- BEGIN GENERATED DECISION TOKENS -----

  # DECISION TOKENS — generated by `scripts/build-decisions.py`
  # Source: @gouvfr/dsfr@1.13.0/dist/dsfr.css
  # Tier 1+2 (≥5 component-CSS references). Do not
  # edit by hand — re-run the script and paste the output.

  # ---- background ----
  background-action-high-blue-france:                "{colors.blue-france-sun-113-625}"   # used 41×
  background-action-high-blue-france-active:         "{colors.blue-france-sun-113-625-active}"   # used 3×
  background-action-high-blue-france-hover:          "{colors.blue-france-sun-113-625-hover}"   # used 3×
  background-action-high-error:                      "{colors.error-425-625}"   # used 2×
  background-action-high-error-active:               "{colors.error-425-625-active}"   # used 2×
  background-action-high-error-hover:                "{colors.error-425-625-hover}"   # used 2×
  background-action-high-grey:                       "{colors.grey-200-850}"   # used 2×
  background-action-high-grey-active:                "{colors.grey-200-850-active}"   # used 2×
  background-action-high-grey-hover:                 "{colors.grey-200-850-hover}"   # used 2×
  background-action-low-blue-france:                 "{colors.blue-france-925-125}"   # used 5×
  background-action-low-blue-france-active:          "{colors.blue-france-925-125-active}"   # used 3×
  background-action-low-blue-france-hover:           "{colors.blue-france-925-125-hover}"   # used 3×
  background-active-blue-france:                     "{colors.blue-france-sun-113-625}"   # used 23×
  background-active-blue-france-active:              "{colors.blue-france-sun-113-625-active}"   # used 7×
  background-active-blue-france-hover:               "{colors.blue-france-sun-113-625-hover}"   # used 7×
  background-alt-blue-france:                        "{colors.blue-france-975-75}"   # used 1×
  background-alt-blue-france-active:                 "{colors.blue-france-975-75-active}"   # used 1×
  background-alt-blue-france-hover:                  "{colors.blue-france-975-75-hover}"   # used 1×
  background-alt-grey:                               "{colors.grey-975-75}"   # used 6×
  background-alt-grey-active:                        "{colors.grey-975-75-active}"   # used 6×
  background-alt-grey-hover:                         "{colors.grey-975-75-hover}"   # used 6×
  background-contrast-beige-gris-galet:              "{colors.beige-gris-galet-950-100}"   # used 4×
  background-contrast-beige-gris-galet-active:       "{colors.beige-gris-galet-950-100-active}"   # used 4×
  background-contrast-beige-gris-galet-hover:        "{colors.beige-gris-galet-950-100-hover}"   # used 4×
  background-contrast-blue-cumulus:                  "{colors.blue-cumulus-950-100}"   # used 4×
  background-contrast-blue-cumulus-active:           "{colors.blue-cumulus-950-100-active}"   # used 4×
  background-contrast-blue-cumulus-hover:            "{colors.blue-cumulus-950-100-hover}"   # used 4×
  background-contrast-blue-ecume:                    "{colors.blue-ecume-950-100}"   # used 4×
  background-contrast-blue-ecume-active:             "{colors.blue-ecume-950-100-active}"   # used 4×
  background-contrast-blue-ecume-hover:              "{colors.blue-ecume-950-100-hover}"   # used 4×
  background-contrast-brown-cafe-creme:              "{colors.brown-cafe-creme-950-100}"   # used 4×
  background-contrast-brown-cafe-creme-active:       "{colors.brown-cafe-creme-950-100-active}"   # used 4×
  background-contrast-brown-cafe-creme-hover:        "{colors.brown-cafe-creme-950-100-hover}"   # used 4×
  background-contrast-brown-caramel:                 "{colors.brown-caramel-950-100}"   # used 4×
  background-contrast-brown-caramel-active:          "{colors.brown-caramel-950-100-active}"   # used 4×
  background-contrast-brown-caramel-hover:           "{colors.brown-caramel-950-100-hover}"   # used 4×
  background-contrast-brown-opera:                   "{colors.brown-opera-950-100}"   # used 4×
  background-contrast-brown-opera-active:            "{colors.brown-opera-950-100-active}"   # used 4×
  background-contrast-brown-opera-hover:             "{colors.brown-opera-950-100-hover}"   # used 4×
  background-contrast-error:                         "{colors.error-950-100}"   # used 2×
  background-contrast-error-active:                  "{colors.error-950-100-active}"   # used 2×
  background-contrast-error-hover:                   "{colors.error-950-100-hover}"   # used 2×
  background-contrast-green-archipel:                "{colors.green-archipel-950-100}"   # used 4×
  background-contrast-green-archipel-active:         "{colors.green-archipel-950-100-active}"   # used 4×
  background-contrast-green-archipel-hover:          "{colors.green-archipel-950-100-hover}"   # used 4×
  background-contrast-green-bourgeon:                "{colors.green-bourgeon-950-100}"   # used 4×
  background-contrast-green-bourgeon-active:         "{colors.green-bourgeon-950-100-active}"   # used 4×
  background-contrast-green-bourgeon-hover:          "{colors.green-bourgeon-950-100-hover}"   # used 4×
  background-contrast-green-emeraude:                "{colors.green-emeraude-950-100}"   # used 4×
  background-contrast-green-emeraude-active:         "{colors.green-emeraude-950-100-active}"   # used 4×
  background-contrast-green-emeraude-hover:          "{colors.green-emeraude-950-100-hover}"   # used 4×
  background-contrast-green-menthe:                  "{colors.green-menthe-950-100}"   # used 4×
  background-contrast-green-menthe-active:           "{colors.green-menthe-950-100-active}"   # used 4×
  background-contrast-green-menthe-hover:            "{colors.green-menthe-950-100-hover}"   # used 4×
  background-contrast-green-tilleul-verveine:        "{colors.green-tilleul-verveine-950-100}"   # used 4×
  background-contrast-green-tilleul-verveine-active: "{colors.green-tilleul-verveine-950-100-active}"   # used 4×
  background-contrast-green-tilleul-verveine-hover:  "{colors.green-tilleul-verveine-950-100-hover}"   # used 4×
  background-contrast-grey:                          "{colors.grey-950-100}"   # used 13×
  background-contrast-grey-active:                   "{colors.grey-950-100-active}"   # used 10×
  background-contrast-grey-hover:                    "{colors.grey-950-100-hover}"   # used 10×
  background-contrast-info:                          "{colors.info-950-100}"   # used 3×
  background-contrast-info-active:                   "{colors.info-950-100-active}"   # used 2×
  background-contrast-info-hover:                    "{colors.info-950-100-hover}"   # used 2×
  background-contrast-orange-terre-battue:           "{colors.orange-terre-battue-950-100}"   # used 4×
  background-contrast-orange-terre-battue-active:    "{colors.orange-terre-battue-950-100-active}"   # used 4×
  background-contrast-orange-terre-battue-hover:     "{colors.orange-terre-battue-950-100-hover}"   # used 4×
  background-contrast-pink-macaron:                  "{colors.pink-macaron-950-100}"   # used 4×
  background-contrast-pink-macaron-active:           "{colors.pink-macaron-950-100-active}"   # used 4×
  background-contrast-pink-macaron-hover:            "{colors.pink-macaron-950-100-hover}"   # used 4×
  background-contrast-pink-tuile:                    "{colors.pink-tuile-950-100}"   # used 4×
  background-contrast-pink-tuile-active:             "{colors.pink-tuile-950-100-active}"   # used 4×
  background-contrast-pink-tuile-hover:              "{colors.pink-tuile-950-100-hover}"   # used 4×
  background-contrast-purple-glycine:                "{colors.purple-glycine-950-100}"   # used 4×
  background-contrast-purple-glycine-active:         "{colors.purple-glycine-950-100-active}"   # used 4×
  background-contrast-purple-glycine-hover:          "{colors.purple-glycine-950-100-hover}"   # used 4×
  background-contrast-warning:                       "{colors.warning-950-100}"   # used 2×
  background-contrast-warning-active:                "{colors.warning-950-100-active}"   # used 2×
  background-contrast-warning-hover:                 "{colors.warning-950-100-hover}"   # used 2×
  background-contrast-yellow-moutarde:               "{colors.yellow-moutarde-950-100}"   # used 5×
  background-contrast-yellow-moutarde-active:        "{colors.yellow-moutarde-950-100-active}"   # used 5×
  background-contrast-yellow-moutarde-hover:         "{colors.yellow-moutarde-950-100-hover}"   # used 5×
  background-contrast-yellow-tournesol:              "{colors.yellow-tournesol-950-100}"   # used 4×
  background-contrast-yellow-tournesol-active:       "{colors.yellow-tournesol-950-100-active}"   # used 4×
  background-contrast-yellow-tournesol-hover:        "{colors.yellow-tournesol-950-100-hover}"   # used 4×
  background-default-grey:                           "{colors.grey-1000-50}"   # used 18×
  background-default-grey-active:                    "{colors.grey-1000-50-active}"   # used 15×
  background-default-grey-hover:                     "{colors.grey-1000-50-hover}"   # used 15×
  background-disabled-grey:                          "{colors.grey-925-125}"   # used 73×
  background-elevated-grey:                          "{colors.grey-1000-75}"   # used 0×
  background-flat-error:                             "{colors.error-425-625}"   # used 4×
  background-flat-info:                              "{colors.info-425-625}"   # used 2×
  background-flat-success:                           "{colors.success-425-625}"   # used 2×
  background-flat-warning:                           "{colors.warning-425-625}"   # used 2×
  background-lifted-grey:                            "{colors.grey-1000-75}"   # used 3×
  background-lifted-grey-active:                     "{colors.grey-1000-75-active}"   # used 3×
  background-lifted-grey-hover:                      "{colors.grey-1000-75-hover}"   # used 3×
  background-open-blue-france:                       "{colors.blue-france-925-125}"   # used 7×
  background-open-blue-france-active:                "{colors.blue-france-925-125-active}"   # used 5×
  background-open-blue-france-hover:                 "{colors.blue-france-925-125-hover}"   # used 5×
  background-raised-grey:                            "{colors.grey-1000-75}"   # used 6×
  background-raised-grey-active:                     "{colors.grey-1000-75-active}"   # used 6×
  background-raised-grey-hover:                      "{colors.grey-1000-75-hover}"   # used 6×
  # Stacks `--shadow` over `--grey` — see `.fr-card--shadow.fr-card--grey`.
  background-contrast-raised-grey:                   "{colors.grey-950-125}"   # used 1×
  background-contrast-raised-grey-active:            "{colors.grey-950-125-active}"   # used 1×
  background-contrast-raised-grey-hover:             "{colors.grey-950-125-hover}"   # used 1×

  # ---- text ----
  text-action-high-blue-france:                      "{colors.blue-france-sun-113-625}"   # used 34×
  text-action-high-grey:                             "{colors.grey-50-1000}"   # used 6×
  text-active-blue-france:                           "{colors.blue-france-sun-113-625}"   # used 8×
  text-active-grey:                                  "{colors.grey-50-1000}"   # used 0×
  text-default-error:                                "{colors.error-425-625}"   # used 10×
  text-default-grey:                                 "{colors.grey-200-850}"   # used 9×
  text-default-info:                                 "{colors.info-425-625}"   # used 7×
  text-default-success:                              "{colors.success-425-625}"   # used 9×
  text-disabled-grey:                                "{colors.grey-625-425}"   # used 59×
  text-inverted-blue-france:                         "{colors.blue-france-975-sun-113}"   # used 5×
  text-inverted-grey:                                "{colors.grey-1000-50}"   # used 6×
  text-label-grey:                                   "{colors.grey-50-1000}"   # used 8×
  text-mention-grey:                                 "{colors.grey-425-625}"   # used 19×
  text-title-blue-france:                            "{colors.blue-france-sun-113-625}"   # used 0×
  text-title-grey:                                   "{colors.grey-50-1000}"   # used 19×

  # ---- border ----
  border-action-high-blue-france:                    "{colors.blue-france-sun-113-625}"   # used 83×
  border-active-blue-france:                         "{colors.blue-france-sun-113-625}"   # used 54×
  border-contrast-grey:                              "{colors.grey-625-425}"   # used 22×
  border-default-beige-gris-galet:                   "{colors.beige-gris-galet-main-702}"   # used 14×
  border-default-blue-cumulus:                       "{colors.blue-cumulus-main-526}"   # used 14×
  border-default-blue-ecume:                         "{colors.blue-ecume-main-400}"   # used 14×
  border-default-blue-france:                        "{colors.blue-france-main-525}"   # used 6×
  border-default-brown-cafe-creme:                   "{colors.brown-cafe-creme-main-782}"   # used 14×
  border-default-brown-caramel:                      "{colors.brown-caramel-main-648}"   # used 14×
  border-default-brown-opera:                        "{colors.brown-opera-main-680}"   # used 14×
  border-default-green-archipel:                     "{colors.green-archipel-main-557}"   # used 14×
  border-default-green-bourgeon:                     "{colors.green-bourgeon-main-640}"   # used 14×
  border-default-green-emeraude:                     "{colors.green-emeraude-main-632}"   # used 14×
  border-default-green-menthe:                       "{colors.green-menthe-main-548}"   # used 14×
  border-default-green-tilleul-verveine:             "{colors.green-tilleul-verveine-main-707}"   # used 14×
  border-default-grey:                               "{colors.grey-900-175}"   # used 177×
  border-default-orange-terre-battue:                "{colors.orange-terre-battue-main-645}"   # used 14×
  border-default-pink-macaron:                       "{colors.pink-macaron-main-689}"   # used 14×
  border-default-pink-tuile:                         "{colors.pink-tuile-main-556}"   # used 14×
  border-default-purple-glycine:                     "{colors.purple-glycine-main-494}"   # used 14×
  border-default-yellow-moutarde:                    "{colors.yellow-moutarde-main-679}"   # used 14×
  border-default-yellow-tournesol:                   "{colors.yellow-tournesol-main-731}"   # used 14×
  border-disabled-grey:                              "{colors.grey-925-125}"   # used 19×
  border-plain-error:                                "{colors.error-425-625}"   # used 95×
  border-plain-grey:                                 "{colors.grey-200-850}"   # used 26×
  border-plain-info:                                 "{colors.info-425-625}"   # used 23×
  border-plain-success:                              "{colors.success-425-625}"   # used 93×
  border-plain-warning:                              "{colors.warning-425-625}"   # used 8×

  # ---- artwork ----
  artwork-major-blue-france:                         "{colors.blue-france-sun-113-625}"   # used 1×
  artwork-major-blue-france-active:                  "{colors.blue-france-sun-113-625-active}"   # used 0×
  artwork-major-blue-france-hover:                   "{colors.blue-france-sun-113-625-hover}"   # used 0×
  artwork-minor-blue-france:                         "{colors.blue-france-main-525}"   # used 1×
    # ----- END GENERATED DECISION TOKENS -----

  # Literal hex (not a token reference) — DSFR's focus ring is set via the
  # `focus` decision token but compiles to the same hex regardless of theme.
  focus-ring:                      "#0a76f6"

typography:
  # ===========================================================
  # Marianne — sans-serif, the primary government typeface.
  # Sizes mirror the canonical DSFR ladder; values are the
  # DESKTOP attributes (the docs' "Attributs desktop" column).
  # Mobile values are exposed as `*-mobile` companion tokens
  # below so the responsive ladder is fully captured in YAML.
  # ===========================================================

  # ---- Titres alternatifs (display sizes — fr-display--*) ----
  # Editorial / hero use only. Apply via the `fr-display--{size}`
  # utility class on any heading element.
  display-xl:
    fontFamily: Marianne
    fontSize: 5rem           # 80px (desktop)
    fontWeight: 700
    lineHeight: 5.5rem       # 88px
  display-lg:
    fontFamily: Marianne
    fontSize: 4.5rem         # 72px (desktop)
    fontWeight: 700
    lineHeight: 5rem         # 80px
  display-md:
    fontFamily: Marianne
    fontSize: 4rem           # 64px (desktop)
    fontWeight: 700
    lineHeight: 4.5rem       # 72px
  display-sm:
    fontFamily: Marianne
    fontSize: 3.5rem         # 56px (desktop)
    fontWeight: 700
    lineHeight: 4rem         # 64px
  display-xs:
    fontFamily: Marianne
    fontSize: 3rem           # 48px (desktop)
    fontWeight: 700
    lineHeight: 3.5rem       # 56px

  # ---- Titres (semantic headings — h1…h6 / fr-h1…fr-h6) ----
  h1:
    fontFamily: Marianne
    fontSize: 2.5rem         # 40px (desktop)
    fontWeight: 700
    lineHeight: 3rem         # 48px
  h2:
    fontFamily: Marianne
    fontSize: 2rem           # 32px (desktop)
    fontWeight: 700
    lineHeight: 2.5rem       # 40px
  h3:
    fontFamily: Marianne
    fontSize: 1.75rem        # 28px (desktop)
    fontWeight: 700
    lineHeight: 2.25rem      # 36px
  h4:
    fontFamily: Marianne
    fontSize: 1.5rem         # 24px (desktop)
    fontWeight: 700
    lineHeight: 2rem         # 32px
  h5:
    fontFamily: Marianne
    fontSize: 1.375rem       # 22px (desktop)
    fontWeight: 700
    lineHeight: 1.75rem      # 28px
  h6:
    fontFamily: Marianne
    fontSize: 1.25rem        # 20px (desktop)
    fontWeight: 700
    lineHeight: 1.75rem      # 28px

  # ---- Body / paragraph styles (size-stable across breakpoints) ----
  body-xl:                   # also: lead — fr-text--xl / fr-text--lead
    fontFamily: Marianne
    fontSize: 1.25rem        # 20px
    fontWeight: 400
    lineHeight: 2rem         # 32px
  body-lg:                   # fr-text--lg
    fontFamily: Marianne
    fontSize: 1.125rem       # 18px
    fontWeight: 400
    lineHeight: 1.75rem      # 28px
  body-md:                   # fr-text--md (default body size)
    fontFamily: Marianne
    fontSize: 1rem           # 16px
    fontWeight: 400
    lineHeight: 1.5rem       # 24px
  body-sm:                   # fr-text--sm
    fontFamily: Marianne
    fontSize: 0.875rem       # 14px
    fontWeight: 400
    lineHeight: 1.5rem       # 24px
  body-xs:                   # fr-text--xs
    fontFamily: Marianne
    fontSize: 0.75rem        # 12px
    fontWeight: 400
    lineHeight: 1.25rem      # 20px
  label:
    fontFamily: Marianne
    fontSize: 0.875rem       # 14px
    fontWeight: 700
    lineHeight: 1.5rem       # 24px

  # ---- Spectral — serif, secondary; via the `fr-text--alt` class. ----
  body-md-alt:
    fontFamily: Spectral
    fontSize: 1rem           # 16px
    fontWeight: 400
    lineHeight: 1.5rem       # 24px
  body-sm-alt:
    fontFamily: Spectral
    fontSize: 0.875rem       # 14px
    fontWeight: 400
    lineHeight: 1.5rem       # 24px

  # ===========================================================
  # Mobile companion tokens (viewports < 48em / 768px).
  # Apply automatically via DSFR's `fr-h*` and `fr-display--*`
  # utility classes, which carry @media rules. Listed here so
  # agents emitting custom (non-utility-class) markup can pick
  # the correct size manually for the mobile breakpoint.
  # ===========================================================
  display-xl-mobile:
    fontFamily: Marianne
    fontSize: 4.5rem         # 72px
    fontWeight: 700
    lineHeight: 5rem         # 80px
  display-lg-mobile:
    fontFamily: Marianne
    fontSize: 4rem           # 64px
    fontWeight: 700
    lineHeight: 4.5rem       # 72px
  display-md-mobile:
    fontFamily: Marianne
    fontSize: 3.5rem         # 56px
    fontWeight: 700
    lineHeight: 4rem         # 64px
  display-sm-mobile:
    fontFamily: Marianne
    fontSize: 3rem           # 48px
    fontWeight: 700
    lineHeight: 3.5rem       # 56px
  display-xs-mobile:
    fontFamily: Marianne
    fontSize: 2.5rem         # 40px
    fontWeight: 700
    lineHeight: 3rem         # 48px
  h1-mobile:
    fontFamily: Marianne
    fontSize: 2rem           # 32px
    fontWeight: 700
    lineHeight: 2.5rem       # 40px
  h2-mobile:
    fontFamily: Marianne
    fontSize: 1.75rem        # 28px
    fontWeight: 700
    lineHeight: 2.25rem      # 36px
  h3-mobile:
    fontFamily: Marianne
    fontSize: 1.5rem         # 24px
    fontWeight: 700
    lineHeight: 2rem         # 32px
  h4-mobile:
    fontFamily: Marianne
    fontSize: 1.375rem       # 22px
    fontWeight: 700
    lineHeight: 1.75rem      # 28px
  h5-mobile:
    fontFamily: Marianne
    fontSize: 1.25rem        # 20px
    fontWeight: 700
    lineHeight: 1.75rem      # 28px
  h6-mobile:
    fontFamily: Marianne
    fontSize: 1.125rem       # 18px
    fontWeight: 700
    lineHeight: 1.5rem       # 24px

rounded:
  # The DSFR has no fundamentals-level border-radius scale —
  # corners are square by convention and the few exceptions are
  # specified at the component level. These three tokens cover
  # every documented exception:
  #   - `none` is the default for ~all components
  #   - `sm`   is used only for the search input's top corners
  #   - `pill` is used for tags, badges, the toggle switch
  none: 0px
  sm:   0.25rem    # 4px — search input top corners only
  pill: 9999px     # tags, badges, toggle switch

spacing:
  # ===========================================================
  # DSFR `v` unit: 1v = 0.25rem = 4px. The ladder runs from 0v
  # through 32v in 1v steps, plus two fractional steps (0-5v,
  # 1-5v) for hairline spacing. Every step has matching DSFR
  # utility classes (e.g. `fr-mb-Nv`, `fr-py-Nv`, `fr-gap-Nv`)
  # so the full ladder is enumerated here for reference.
  #
  # The Figma / designer tooling also references a "W" unit
  # where 1W = 2v = 8px. The W-aligned rows below are flagged
  # in the trailing comment when the value also corresponds to
  # an integer number of W; the canonical token name is always
  # `Nv` regardless of W alignment.
  #
  # The DSFR also exposes a parallel negative ladder
  # (`n0-5v` … `n8v`) for negative margins, but it is rarely
  # used in practice and intentionally omitted here. Agents
  # needing a negative offset should emit the corresponding
  # `fr-m-nNv` utility class directly.
  # ===========================================================
  0v:    0px           # 0
  0-5v:  0.125rem      # 2px   — hairline
  1v:    0.25rem       # 4px
  1-5v:  0.375rem      # 6px
  2v:    0.5rem        # 8px   (1W)
  3v:    0.75rem       # 12px
  4v:    1rem          # 16px  (2W) — standard inter-component gap
  5v:    1.25rem       # 20px
  6v:    1.5rem        # 24px  (3W) — typical card padding
  7v:    1.75rem       # 28px
  8v:    2rem          # 32px  (4W) — section spacing
  9v:    2.25rem       # 36px
  10v:   2.5rem        # 40px  (5W)
  11v:   2.75rem       # 44px
  12v:   3rem          # 48px  (6W)
  13v:   3.25rem       # 52px
  14v:   3.5rem        # 56px  (7W)
  15v:   3.75rem       # 60px
  16v:   4rem          # 64px  (8W)
  17v:   4.25rem       # 68px
  18v:   4.5rem        # 72px  (9W)
  19v:   4.75rem       # 76px
  20v:   5rem          # 80px  (10W)
  21v:   5.25rem       # 84px
  22v:   5.5rem        # 88px  (11W)
  23v:   5.75rem       # 92px
  24v:   6rem          # 96px  (12W)
  25v:   6.25rem       # 100px (≈ 12.5W)
  26v:   6.5rem        # 104px (13W)
  27v:   6.75rem       # 108px
  28v:   7rem          # 112px (14W)
  29v:   7.25rem       # 116px
  30v:   7.5rem        # 120px (15W)
  31v:   7.75rem       # 124px
  32v:   8rem          # 128px (16W)

  # Semantic spacing aliases used by typography tokens. Mirrors
  # the canonical DSFR `--title-spacing` / `--display-spacing`
  # CSS variables (which expand to `0 0 1.5rem` / `0 0 2rem`).
  # Captured here as primitives so agents have a single
  # margin-bottom value per role.
  title-margin:   1.5rem   # 24px (= 6v / 3W) — h1…h6 bottom margin
  display-margin: 2rem     # 32px (= 8v / 4W) — fr-display--* bottom margin

components:
  # ============================================================
  # ACTIONS — Buttons
  #
  # Four base variants × four states (default / hover / active /
  # disabled) plus three sizes. The schema only recognises the
  # core sub-tokens (backgroundColor / textColor / typography /
  # rounded / padding / height); border styling, font-weight 500,
  # and the canonical `box-shadow: inset` border-without-layout-
  # shift trick all live in the `### Actions` prose below.
  #
  # The disabled state collapses every variant to the same
  # background/text colours (`background-disabled-grey` /
  # `text-disabled-grey`) and drops the inset border, so all
  # four `*-disabled` entries share a single colour pair.
  #
  # Sizes are expressed as deltas (only the properties that
  # change vs the default `md`). They compose with any base
  # variant: `button-primary` + `button-sm` = primary small.
  # ============================================================

  # ---- Variant 1 / 4 — Primary (`fr-btn`) ----
  button-primary:
    backgroundColor: "{colors.background-action-high-blue-france}"
    textColor:       "{colors.text-inverted-blue-france}"
    typography:      "{typography.body-md}"
    rounded:         "{rounded.none}"
    padding:         "8px 16px"
    height:          40px
  button-primary-hover:
    backgroundColor: "{colors.background-action-high-blue-france-hover}"
    textColor:       "{colors.text-inverted-blue-france}"
  button-primary-active:
    backgroundColor: "{colors.background-action-high-blue-france-active}"
    textColor:       "{colors.text-inverted-blue-france}"
  button-primary-disabled:
    backgroundColor: "{colors.background-disabled-grey}"
    textColor:       "{colors.text-disabled-grey}"

  # ---- Variant 2 / 4 — Secondary (`fr-btn fr-btn--secondary`).
  #      Transparent fill + 1 px `border-action-high-blue-france`
  #      inset border (drawn via box-shadow per the prose). ----
  button-secondary:
    backgroundColor: "transparent"
    textColor:       "{colors.text-action-high-blue-france}"
    typography:      "{typography.body-md}"
    rounded:         "{rounded.none}"
    padding:         "8px 16px"
    height:          40px
  button-secondary-hover:
    # The DSFR overlays a faint translucent black on hover; the
    # opaque equivalent on the light theme is blue-france-950-100-hover.
    backgroundColor: "{colors.blue-france-950-100-hover}"
    textColor:       "{colors.text-action-high-blue-france}"
  button-secondary-active:
    backgroundColor: "{colors.blue-france-950-100-active}"
    textColor:       "{colors.text-action-high-blue-france}"
  button-secondary-disabled:
    backgroundColor: "{colors.background-disabled-grey}"
    textColor:       "{colors.text-disabled-grey}"

  # ---- Variant 3 / 4 — Tertiary (`fr-btn fr-btn--tertiary`).
  #      Transparent fill + 1 px `border-default-grey` inset
  #      border (drawn via box-shadow per the prose). ----
  button-tertiary:
    backgroundColor: "transparent"
    textColor:       "{colors.text-action-high-blue-france}"
    typography:      "{typography.body-md}"
    rounded:         "{rounded.none}"
    padding:         "8px 16px"
    height:          40px
  button-tertiary-hover:
    backgroundColor: "{colors.background-alt-grey-hover}"
    textColor:       "{colors.text-action-high-blue-france}"
  button-tertiary-active:
    backgroundColor: "{colors.background-alt-grey-active}"
    textColor:       "{colors.text-action-high-blue-france}"
  button-tertiary-disabled:
    backgroundColor: "{colors.background-disabled-grey}"
    textColor:       "{colors.text-disabled-grey}"

  # ---- Variant 4 / 4 — Tertiary, no outline
  #      (`fr-btn fr-btn--tertiary fr-btn--no-outline`).
  #      Same as tertiary but without the inset border. Underlies
  #      the DSFR's pre-baked icon buttons (close, display, team,
  #      briefcase, account) which are not separate decisions —
  #      just convenience shorthands over this variant. ----
  button-tertiary-no-outline:
    backgroundColor: "transparent"
    textColor:       "{colors.text-action-high-blue-france}"
    typography:      "{typography.body-md}"
    rounded:         "{rounded.none}"
    padding:         "8px 16px"
    height:          40px
  button-tertiary-no-outline-hover:
    backgroundColor: "{colors.background-alt-grey-hover}"
    textColor:       "{colors.text-action-high-blue-france}"
  button-tertiary-no-outline-active:
    backgroundColor: "{colors.background-alt-grey-active}"
    textColor:       "{colors.text-action-high-blue-france}"
  button-tertiary-no-outline-disabled:
    backgroundColor: "transparent"
    textColor:       "{colors.text-disabled-grey}"

  # ---- Sizes — deltas applied on top of any variant.
  #      Default size is the `button-*` base (40 px height,
  #      body-md type, 8px/16px padding); sm and lg override only
  #      the dimensional properties. ----
  button-sm:
    typography:      "{typography.body-sm}"
    height:          32px
    padding:         "4px 12px"
  button-lg:
    typography:      "{typography.body-lg}"
    height:          48px
    padding:         "8px 24px"

  # ============================================================
  # FORMS — input, select, checkbox, radio, toggle
  # ============================================================
  # ---- Input (`fr-input`)
  #
  # The input lives on a contrast-grey surface with an
  # asymmetric border-radius (sm at the top corners, none at the
  # bottom) and a 2 px bottom underline drawn via
  # `box-shadow: inset 0 -2px 0 0 <colour>`. The schema only
  # captures a single `rounded` value and no shadow/underline;
  # the underline-by-state mapping (grey / red / green /
  # disabled-grey) lives in the `### Forms` prose. Focus is
  # handled by the global focus ring and adds no token
  # overrides, so there is no `input-focus` entry.
  #
  # State entries record only the colour overrides that apply
  # to the input surface itself — accompanying `<label>` and
  # `.fr-error-text` / `.fr-valid-text` colour shifts are
  # documented in prose.
  # ----
  input:
    backgroundColor: "{colors.background-contrast-grey}"
    textColor:       "{colors.text-default-grey}"
    typography:      "{typography.body-md}"
    rounded:         "{rounded.sm}"
    padding:         "8px 16px"
    height:          40px
  input-error:
    backgroundColor: "{colors.background-contrast-grey}"
    textColor:       "{colors.text-default-grey}"
  input-success:
    backgroundColor: "{colors.background-contrast-grey}"
    textColor:       "{colors.text-default-grey}"
  input-disabled:
    backgroundColor: "{colors.background-contrast-grey}"
    textColor:       "{colors.text-disabled-grey}"

  # ---- Select (`fr-select`)
  #
  # The select shares every surface, type, underline and state
  # convention with the input — same `.fr-select-group--error /
  # --valid / --disabled` modifiers, same `box-shadow: inset 0
  # -2px 0 0 …` underline, same asymmetric corners. Differences
  # vs input:
  #   • Right padding is 2.5 rem (vs 1 rem) to leave room for
  #     a 1 rem chevron-down SVG drawn via `background-image`
  #     and anchored 1 rem from the right edge (mirror of the
  #     date-input technique).
  #   • Padding entry below records the LEFT/RIGHT base only,
  #     since the schema does not capture per-side padding.
  # ----
  select:
    backgroundColor: "{colors.background-contrast-grey}"
    textColor:       "{colors.text-default-grey}"
    typography:      "{typography.body-md}"
    rounded:         "{rounded.sm}"
    padding:         "8px 16px"
    height:          40px
  select-error:
    backgroundColor: "{colors.background-contrast-grey}"
    textColor:       "{colors.text-default-grey}"
  select-success:
    backgroundColor: "{colors.background-contrast-grey}"
    textColor:       "{colors.text-default-grey}"
  select-disabled:
    backgroundColor: "{colors.background-contrast-grey}"
    textColor:       "{colors.text-disabled-grey}"

  # ---- Checkbox (`fr-checkbox-group`)
  #
  # Default size is 24 px (1.5 rem); a sm modifier shrinks it
  # to 16 px (1 rem). The box uses `rounded.sm` (0.25 rem) and
  # carries the `border-action-high-blue-france` colour as its
  # outline. Checked fill uses `background-active-blue-france`
  # with a white check SVG (light) / blue check SVG (dark).
  #
  # Group states (`.fr-fieldset--error / --valid` and
  # `<fieldset disabled>`) act on the legend and labels — the
  # box itself stays mostly the same. The error/success state
  # also draws a 2 px coloured strip on the left of the
  # fieldset, matching the input/select group pattern.
  # ----
  checkbox:
    backgroundColor: "{colors.background-default-grey}"
    textColor:       "{colors.text-default-grey}"
    rounded:         "{rounded.sm}"
    size:            24px
  checkbox-sm:
    backgroundColor: "{colors.background-default-grey}"
    textColor:       "{colors.text-default-grey}"
    rounded:         "{rounded.sm}"
    size:            16px
  checkbox-checked:
    backgroundColor: "{colors.text-action-high-blue-france}"
    textColor:       "{colors.text-inverted-grey}"
  checkbox-disabled:
    backgroundColor: "{colors.background-disabled-grey}"
    textColor:       "{colors.text-disabled-grey}"
  checkbox-error:
    backgroundColor: "{colors.background-default-grey}"
    textColor:       "{colors.text-default-error}"
  checkbox-success:
    backgroundColor: "{colors.background-default-grey}"
    textColor:       "{colors.text-default-success}"

  # ---- Radio (`fr-radio-group`)
  #
  # Mirror of the checkbox structure: same default 24 px / sm
  # 16 px sizes, same `border-action-high-blue-france` outline,
  # same group-state mechanics (legend + 2 px left strip + ring
  # colour swap on error/success). The differences:
  #   • `rounded.pill` (full circle) instead of rounded.sm
  #   • Checked state replaces the *fill* with a small inner
  #     dot (radial-gradient) rather than a check SVG
  #   • The inner dot stays blue even in error/success groups
  #     — only the *ring* turns red/green; canon does it via
  #     stacked radial-gradients
  #   • `radio-rich` is a card-like composition unique to this
  #     component: a bordered tile with a pictogram + label;
  #     the radio circle is anchored to the top-right and the
  #     entire card border lights up blue when selected.
  # ----
  radio:
    backgroundColor: "{colors.background-default-grey}"
    textColor:       "{colors.text-default-grey}"
    rounded:         "{rounded.pill}"
    size:            24px
  radio-sm:
    backgroundColor: "{colors.background-default-grey}"
    textColor:       "{colors.text-default-grey}"
    rounded:         "{rounded.pill}"
    size:            16px
  radio-checked:
    backgroundColor: "{colors.text-action-high-blue-france}"
    textColor:       "{colors.text-inverted-grey}"
  radio-disabled:
    backgroundColor: "{colors.background-disabled-grey}"
    textColor:       "{colors.text-disabled-grey}"
  radio-error:
    backgroundColor: "{colors.background-default-grey}"
    textColor:       "{colors.text-default-error}"
  radio-success:
    backgroundColor: "{colors.background-default-grey}"
    textColor:       "{colors.text-default-success}"
  radio-rich:
    backgroundColor: "{colors.background-default-grey}"
    textColor:       "{colors.text-label-grey}"
    rounded:         "{rounded.none}"
    padding:         "12px 16px"

  # ---- Toggle (`fr-toggle`)
  #
  # The toggle's OFF state is a STROKED track (white interior,
  # 1 px blue-france border) — NOT a filled grey track. Both
  # the track and the thumb carry that 1 px border separately;
  # turning the toggle ON fills the track with `text-action-
  # high-blue-france` and reveals a small blue check ✓ inside
  # the still-white thumb (which translates +1 rem right).
  #
  # Track 2.5 rem × 1.5 rem (40 × 24 px), border-radius
  # 0.75 rem. Thumb 1.5 rem × 1.5 rem circle. The thumb does
  # not change colour between OFF and ON — only the track does
  # (and an icon appears inside the thumb).
  #
  # Optional axes:
  #   • `toggle-state` — microstate text (Activé / Désactivé)
  #     rendered below the track in `text-active-blue-france`.
  #   • `.fr-toggle--label-left` — flips the order so the track
  #     ends up flush right.
  #   • `.fr-toggle--border-bottom` — adds a 1 px bottom rule;
  #     used to separate toggles in a fieldset.
  # ----
  toggle:
    backgroundColor: "{colors.background-default-grey}"
    textColor:       "{colors.text-label-grey}"
    rounded:         "{rounded.pill}"
    width:           40px
    height:          24px
  toggle-on:
    backgroundColor: "{colors.text-action-high-blue-france}"
    textColor:       "{colors.text-inverted-grey}"
  toggle-disabled:
    backgroundColor: "{colors.background-default-grey}"
    textColor:       "{colors.text-disabled-grey}"
  toggle-error:
    backgroundColor: "{colors.background-default-grey}"
    textColor:       "{colors.text-default-error}"
  toggle-success:
    backgroundColor: "{colors.background-default-grey}"
    textColor:       "{colors.text-default-success}"
  toggle-state:
    backgroundColor: "{colors.background-default-grey}"
    textColor:       "{colors.text-active-blue-france}"
    typography:      "{typography.body-xs}"

  # ============================================================
  # SURFACES — card, tile
  # ============================================================
  # ---- Card (`fr-card`)
  #
  # The card is composed of:
  #   • `card__img` — illustration / cover (aspect 16/10 in
  #     the demos; canon does not enforce a ratio, but the
  #     placeholder asset is rendered at ~16/10).
  #   • `card__content` — body with the title, optional
  #     description, badges/tags ("start" slot), and the
  #     arrow ("end" slot, anchored bottom-right).
  #
  # Three sizes modulate body padding + title:
  #   • `card-sm` — 24 px padding, 18/24 title
  #   • `card`    — 32 px padding, 20/28 title  (md baseline)
  #   • `card-lg` — 40 px padding, 22/28 title, 16/24 desc
  #
  # The `--md` modifier exists in the canon but is a no-op
  # vs default. Title weight is 700 across all sizes.
  # ----
  card:
    backgroundColor: "{colors.background-default-grey}"
    textColor:       "{colors.text-default-grey}"
    typography:      "{typography.body-md}"
    rounded:         "{rounded.none}"
    padding:         32px
  card-title:
    textColor:       "{colors.text-title-blue-france}"
    typography:      "{typography.h6}"   # 1.25rem / 1.75rem
  card-arrow:
    textColor:       "{colors.text-action-high-blue-france}"
    size:            16px
  card-sm:
    backgroundColor: "{colors.background-default-grey}"
    textColor:       "{colors.text-default-grey}"
    rounded:         "{rounded.none}"
    padding:         24px
  card-lg:
    backgroundColor: "{colors.background-default-grey}"
    textColor:       "{colors.text-default-grey}"
    rounded:         "{rounded.none}"
    padding:         40px
  card-detail:
    textColor:       "{colors.text-mention-grey}"
    typography:      "{typography.body-xs}"   # 0.75rem / 1.25rem
  # Decoration variants — modify the card's background &
  # elevation. They re-emit `--idle / --hover / --active`
  # against a different colour pair, so the standard hover
  # tinting still works inside them.
  card-grey:
    backgroundColor: "{colors.background-contrast-grey}"
    textColor:       "{colors.text-default-grey}"
  # `--shadow` drops the 1 px border, paints with
  # `background-raised-grey`, and adds `filter: drop-shadow(
  # var(--raised-shadow))` — a soft elevated drop on the
  # whole card body. Stacks with `--grey` to use the
  # `background-contrast-raised-grey` colour pair.
  card-shadow:
    backgroundColor: "{colors.background-raised-grey}"
    textColor:       "{colors.text-default-grey}"
  card-shadow-grey:
    backgroundColor: "{colors.background-contrast-raised-grey}"
    textColor:       "{colors.text-default-grey}"
  card-no-background:
    backgroundColor: transparent
    textColor:       "{colors.text-default-grey}"
  card-hover:
    backgroundColor: "{colors.background-alt-grey}"
    textColor:       "{colors.text-default-grey}"

  # ---- Tile (`fr-tile`)
  #
  # The tile is a denser sibling of the card, optimised for
  # category navigation grids and document cards. Compared
  # to the card it adds two distinguishing details:
  #   • A pictogram slot (5 rem default, 3.5 rem in `--sm`,
  #     4 rem in `--horizontal`) instead of a hero image.
  #   • A 4 px coloured rule on the bottom edge — drawn via
  #     a `linear-gradient` background on `__title::before`.
  #     Colour:
  #       · `border-active-blue-france` when the title wraps
  #         an `<a>` or `<button>` (the canon's hint that the
  #         tile is interactive).
  #       · `border-plain-grey` when the title is static
  #         (no-link variant).
  #
  # Sizes (`--sm` only, no `--md` or `--lg`):
  #   • tile-sm — padding 24/24/28 px, title 16/24, picto 56 px
  #   • tile    — padding 32/32/36 px, title 18/24, picto 80 px
  # ----
  tile:
    backgroundColor: "{colors.background-default-grey}"
    textColor:       "{colors.text-default-grey}"
    typography:      "{typography.body-md}"
    rounded:         "{rounded.none}"
    padding:         32px       # 2rem 2rem 2.25rem (top/sides/bottom 36)
  tile-title:
    textColor:       "{colors.text-title-grey}"   # static title
    typography:      "{typography.h6}"            # 1.125rem / 1.5rem in canon (slightly smaller than card)
  tile-title-link:
    textColor:       "{colors.text-action-high-blue-france}"   # title wrapped in <a>/<button>
  tile-detail:
    textColor:       "{colors.text-mention-grey}"
    typography:      "{typography.body-xs}"      # 0.75rem / 1.25rem
  tile-arrow:
    textColor:       "{colors.text-action-high-blue-france}"
    size:            16px                        # 1.5rem in canon for default tile, 1rem in --sm
  # The bottom rule — a 4 px linear-gradient drawn behind
  # `__title`. Colour reflects interactivity.
  tile-rule:
    backgroundColor: "{colors.border-active-blue-france}"
    height:          4px
  tile-rule-static:
    backgroundColor: "{colors.border-plain-grey}"   # no-link variant
    height:          4px
  tile-pictogram:
    size:            80px      # 5rem default, 56px (--sm), 64px (--horizontal), 40px (--sm.--horizontal)
  tile-sm:
    backgroundColor: "{colors.background-default-grey}"
    textColor:       "{colors.text-default-grey}"
    rounded:         "{rounded.none}"
    padding:         24px      # 1.5rem 1.5rem 1.75rem
  # Decoration variants — same pattern as card.
  tile-grey:
    backgroundColor: "{colors.background-contrast-grey}"
    textColor:       "{colors.text-default-grey}"
  tile-shadow:
    backgroundColor: "{colors.background-raised-grey}"
    textColor:       "{colors.text-default-grey}"
  tile-shadow-grey:
    backgroundColor: "{colors.background-contrast-raised-grey}"
    textColor:       "{colors.text-default-grey}"
  tile-no-background:
    backgroundColor: transparent
    textColor:       "{colors.text-default-grey}"
  tile-hover:
    backgroundColor: "{colors.background-default-grey-hover}"
    textColor:       "{colors.text-action-high-blue-france}"

  # ============================================================
  # TAGS & BADGES
  # ============================================================
  tag:
    backgroundColor: "{colors.background-action-low-blue-france}"
    textColor:       "{colors.text-action-high-blue-france}"
    typography:      "{typography.body-sm}"
    rounded:         "{rounded.pill}"
    padding:         12px
    height:          24px
  tag-sm:
    backgroundColor: "{colors.background-action-low-blue-france}"
    textColor:       "{colors.text-action-high-blue-france}"
    typography:      "{typography.body-xs}"
    rounded:         "{rounded.pill}"
    padding:         8px
    height:          20px

  badge:
    backgroundColor: "{colors.background-action-low-blue-france}"
    textColor:       "{colors.text-action-high-blue-france}"
    typography:      "{typography.body-sm}"
    rounded:         "{rounded.pill}"
    padding:         8px
    height:          24px
  badge-success:
    backgroundColor: "{colors.success-975-75}"
    textColor:       "{colors.success-425-625}"
  badge-warning:
    backgroundColor: "{colors.warning-975-75}"
    textColor:       "{colors.text-default-grey}"
  badge-error:
    backgroundColor: "{colors.error-975-75}"
    textColor:       "{colors.text-default-error}"
  badge-info:
    backgroundColor: "{colors.info-975-75}"
    textColor:       "{colors.text-default-info}"

  # ============================================================
  # FEEDBACK — alerts
  # ============================================================
  alert-success:
    backgroundColor: "{colors.success-975-75}"
    textColor:       "{colors.text-default-grey}"
    typography:      "{typography.body-md}"
    rounded:         "{rounded.none}"
    padding:         16px
  alert-warning:
    backgroundColor: "{colors.warning-975-75}"
    textColor:       "{colors.text-default-grey}"
    typography:      "{typography.body-md}"
    rounded:         "{rounded.none}"
    padding:         16px
  alert-error:
    backgroundColor: "{colors.error-975-75}"
    textColor:       "{colors.text-default-grey}"
    typography:      "{typography.body-md}"
    rounded:         "{rounded.none}"
    padding:         16px
  alert-info:
    backgroundColor: "{colors.info-975-75}"
    textColor:       "{colors.text-default-grey}"
    typography:      "{typography.body-md}"
    rounded:         "{rounded.none}"
    padding:         16px

  # ============================================================
  # NAVIGATION — breadcrumb, modal, callout, header, footer
  # ============================================================
  breadcrumb:
    backgroundColor: "{colors.background-default-grey}"
    textColor:       "{colors.text-mention-grey}"
    typography:      "{typography.body-sm}"
    rounded:         "{rounded.none}"
    padding:         16px

  modal:
    backgroundColor: "{colors.background-default-grey}"
    textColor:       "{colors.text-default-grey}"
    typography:      "{typography.body-md}"
    rounded:         "{rounded.none}"
    padding:         32px

  # ---- Callout (`fr-callout`) — Mise en avant
  #
  # A grey-tinted block with a 4 px coloured rule on its
  # left edge, used to draw attention to a notice, key
  # information, or a related action. Three optional slots:
  #   • Icon (set via `fr-icon-*` class on the callout root)
  #   • Title (`__title`, h4-sized)
  #   • Action button (`fr-btn` inside the callout)
  #
  # Default colour pair:
  #   bg = background-contrast-grey
  #   rule = border-default-blue-france (4 px on the left)
  #
  # Thematic colour swap. The callout exposes 17 optional
  # colour variants (`fr-callout--<name>`) that swap both
  # the bg and the rule colour together. Pattern:
  #   bg   = background-contrast-{name}
  #   rule = border-default-{name}
  # Available `<name>`s: green-tilleul-verveine,
  # green-bourgeon, green-emeraude, green-menthe,
  # green-archipel, blue-ecume, blue-cumulus,
  # purple-glycine, pink-macaron, pink-tuile,
  # yellow-tournesol, yellow-moutarde, orange-terre-battue,
  # brown-cafe-creme, brown-caramel, brown-opera,
  # beige-gris-galet.
  # The "Accent Story" in DSFR demos uses `pink-tuile`
  # (a coral/terracotta accent).
  # ----
  callout:
    backgroundColor: "{colors.background-contrast-grey}"
    textColor:       "{colors.text-default-grey}"
    typography:      "{typography.body-lg}"   # 1.125rem / 1.75rem
    rounded:         "{rounded.none}"
    padding:         24px                     # 1.5rem all sides
  callout-title:
    textColor:       "{colors.text-title-grey}"
    typography:      "{typography.h4}"        # 1.375rem / 1.75rem, weight 700
  callout-text:
    textColor:       "{colors.text-default-grey}"
    typography:      "{typography.body-lg}"
  # The 4 px coloured rule on the left edge — drawn via
  # `linear-gradient` background. Width is fixed at 0.25 rem.
  # The colour reflects the thematic variant.
  callout-rule:
    backgroundColor: "{colors.border-default-blue-france}"
  # Pink-tuile is the canon's "Accent Story" preset. All 16
  # other thematic variants follow the same shape — swap the
  # `pink-tuile` segment for any of the names listed above.
  callout-pink-tuile:
    backgroundColor: "{colors.background-contrast-pink-tuile}"
  callout-pink-tuile-rule:
    backgroundColor: "{colors.border-default-pink-tuile}"

  header:
    backgroundColor: "{colors.background-default-grey}"
    textColor:       "{colors.text-default-grey}"
    typography:      "{typography.body-md}"
    rounded:         "{rounded.none}"
    padding:         16px

  footer:
    backgroundColor: "{colors.background-default-grey}"
    textColor:       "{colors.text-default-grey}"
    typography:      "{typography.body-sm}"
    rounded:         "{rounded.none}"
    padding:         32px
---

## Overview

The **Système de Design de l'État** (DSFR) is the official design system of the French Republic — the visual identity, component library, and accessibility framework that every `.gouv.fr` digital service is required to follow under [circulaire n°6411-SG](https://www.systeme-de-design.gouv.fr/version-courante/fr/a-propos/articles-et-actualites/circulaire-d-application-du-7-juillet-2023). It exists to *unify* State websites, to *improve the citizen experience*, and to *guarantee accessibility*.

Visually, the DSFR is **architectural and journalistic**: square corners by default, generous whitespace without ornament, a workhorse sans-serif (Marianne) doing 90% of the typographic load, and a single saturated brand colour — *Bleu France* `#000091` — used as a deliberate signal of officiality and primary action. Decoration is restrained; the State does not fashion-shop. Type and information hierarchy carry the design.

> **Accessibility baseline.** All components target the **RGAA** (*Référentiel Général d'Amélioration de l'Accessibilité*) — France's legal accessibility standard, broadly aligned with **WCAG 2.1 AA**. Concretely:
>
> - Body text contrast ≥ **4.5:1**; large text and UI components ≥ **3:1**.
> - **Visible focus** indicator on every interactive element (the DSFR uses a 2px outer halo in `focus-ring` `#0a76f6`).
> - Touch targets **≥ 44×44 px**.
> - Colour is never the sole carrier of information.

> **Theming.** The DSFR supports a light theme and a dark theme, switched via the `data-fr-scheme` attribute on `<html>` (`"system" | "light" | "dark"`). This `DESIGN.md` encodes the **light theme** in the YAML token graph. See [Colors → Decision tokens](#decision-tokens) below for the dark-theme mappings.

> **Brand & legal scope.** The Marianne wordmark, the *République Française* logo, and the use of *Bleu France* as a State mark are reserved by law for official .gouv.fr services. This file is a derived, machine-readable description; for production .gouv.fr builds always use the canonical [`@gouvfr/dsfr`](https://www.npmjs.com/package/@gouvfr/dsfr) npm package.

## Colors

The DSFR palette is rooted in the French State's graphic charter. Every colour is a **design token** — a transverse name shared across Sketch, Figma, SCSS variables and CSS custom properties. Tokens come in two flavours: **option tokens** (raw palette values) and **decision tokens** (the names UI code references). A well-implemented DSFR site never references option tokens directly.

### Marque de l'État (brand colours)

The brand is built on two anchors — **Bleu France** and **Rouge Marianne** — with white absorbed into the neutrals.

- **Bleu France** `#000091` — the State's primary signal. Reserved for **primary actions** (CTA buttons), **active states**, and **brand surfaces** (the *bloc marque*). Hover `#1212ff`, active `#2323ff`. Light variants step down through `#cacafb` → `#e3e3fd` → `#ececfe` → `#f5f5fe` for low-contrast surfaces (selected list rows, badges, action backgrounds).
- **Rouge Marianne** `#e1000f` — used **sparingly**, attached to the Marianne identity (logo lockups, emphasis in editorial contexts). Hover `#f93f42`, active `#f95a5c`. *Not* a generic destructive-action red — that role belongs to `error` (`#ce0500`).

### Neutrals

A 10-step grey scale handles backgrounds, text, borders, and dividers:

| Role | Light theme | Token |
|------|-------------|-------|
| Page background | `#ffffff` | `grey-1000-50` |
| Alt background | `#f6f6f6` | `grey-975-100` |
| Contrast surface (inputs) | `#eeeeee` | `grey-950-150` |
| Default border | `#dddddd` | `grey-900-175` |
| Mention / placeholder text | `#666666` | `grey-425-625` |
| Body text | `#161616` | `grey-50-1000` |

### System (functional) colours

Reserved for **system feedback only** — never decorative.

| Role | Hex (`-425-625`) | Tinted background (`-950-100`) | Alert background (`-975-75`) |
|------|------------------|-------------------------------|------------------------------|
| Success | `#18753c` | `#b8fec9` | `#dffee6` |
| Warning | `#b34000` | `#ffe9e6` | `#fff4f3` |
| Error   | `#ce0500` | `#ffe9e9` | `#fff4f4` |
| Info    | `#0063cb` | `#e8edff` | `#f4f6ff` |

Each interactive shade (`-425-625` and `-950-100`) ships explicit `-hover` and `-active` states; `-975-75` does not (alerts are not actionable surfaces).

### Illustrative accents

The DSFR ships **12 illustrative families** for complementary editorial use — *tilleul-verveine*, *bourgeon*, *émeraude*, *menthe*, *archipel*, *écume*, *cumulus*, *glycine*, *macaron*, *tuile*, *tournesol*, *moutarde*, *terre-battue*, *café-crème*, *caramel*, *opéra*, *gris-galet*. Rules:

1. **One family per page**, never combined.
2. **Never** for actions or system states (those use Bleu France and the system colours, respectively).
3. Used to add hierarchy, theme a section, or distinguish content categories.

(In the YAML graph these tokens are intentionally **orphaned** — the linter will emit `orphaned-tokens` warnings, which is correct.)

### Decision tokens

UI code must reference **decision tokens**, not option tokens directly. Decision tokens encode *intent* (e.g. "the background of a primary button", "the text colour for a disabled field") rather than a specific shade. They abstract over the light/dark theme split — each decision token references a paired option token whose two values resolve through `data-fr-scheme`.

#### Naming convention

Decision token names follow the canonical DSFR format `<role>-<level>-<family>`:

- **Role** — what kind of style: `background`, `text`, `border`, `artwork`.
- **Level** — the contextual purpose: `default` (the most generic value for the role), `alt` (a light alternative), `contrast` (a more saturated alternative), `action-high` (high-emphasis interactive surface, e.g. primary button), `action-low` (low-emphasis interactive, e.g. tonal button), `active` (currently-selected state), `plain` (saturated solid for status), `disabled`, `open` (expanded/disclosed state), `mention` (lower-priority text), `inverted` (text on a coloured background), `label`, `title`.
- **Family** — which palette the value belongs to: `grey` (neutral), `blue-france` (primary), the four system colours `info`/`success`/`warning`/`error`, or one of the seventeen illustrative-accent families (`green-tilleul-verveine`, `orange-terre-battue`, `pink-macaron`, …).

Examples:

- `background-action-high-blue-france` — the fill of a primary button.
- `border-plain-success` — the solid border of a "success" alert.
- `text-disabled-grey` — body text inside a disabled control.
- `background-disabled-grey` — the surface of a disabled control.
- `text-inverted-grey` — text rendered on top of a saturated coloured surface.

Hover and active states extend the base name with `-hover` / `-active` suffixes, e.g. `background-action-high-blue-france-hover`.

#### Theme handling

A decision token has a single name that resolves to different colour values in light vs dark mode. The translation lives one level down — every decision token references a **paired option token** like `grey-1000-50` whose first value (`#ffffff`) is the light-theme colour and whose second (`#161616`) is the dark-theme colour. Switching `data-fr-scheme="dark"` on `<html>` flips the resolution; the decision token's name never changes.

#### Most-used tokens

| Decision token | Light | Dark | Use |
|---|---|---|---|
| `border-default-grey` | `#dddddd` | `#353535` | Default border (177× — the most-used decision token in DSFR) |
| `border-plain-error` | `#ce0500` | `#ff5655` | Error alerts/borders (95×) |
| `border-plain-success` | `#18753c` | `#27a658` | Success alerts/borders (93×) |
| `border-action-high-blue-france` | `#000091` | `#8585f6` | Primary-button border (83×) |
| `background-disabled-grey` | `#e5e5e5` | `#2a2a2a` | Disabled surfaces (73×) |
| `text-disabled-grey` | `#929292` | `#666666` | Disabled text (59×) |
| `border-active-blue-france` | `#000091` | `#8585f6` | Selected/focused element border (54×) |
| `background-default-grey` | `#ffffff` | `#161616` | Default page surface (48× incl. variants) |
| `background-action-high-blue-france` | `#000091` | `#8585f6` | Primary-button fill (47× incl. variants) |
| `text-action-high-blue-france` | `#000091` | `#8585f6` | Link text, primary-action text (34×) |
| `background-contrast-grey` | `#eeeeee` | `#242424` | Secondary panels, contrast cards (33× incl. variants) |
| `border-plain-grey` | `#3a3a3a` | `#cecece` | Solid neutral borders (26×) |
| `border-plain-info` | `#0063cb` | `#518fff` | Info alerts (23×) |
| `border-contrast-grey` | `#929292` | `#666666` | Contrast-card borders (22×) |
| `text-mention-grey` | `#666666` | `#929292` | Captions, metadata, secondary text (19×) |
| `text-title-grey` | `#161616` | `#ffffff` | Headings on default surfaces (19×) |
| `border-disabled-grey` | `#e5e5e5` | `#2a2a2a` | Disabled-control borders (19×) |
| `focus-ring` | `#0a76f6` | `#4ea7ff` | Focus indicator (theme-stable) |

The full set (~78 Tier 1+2 decision tokens covering 73% of all references in DSFR component CSS) is encoded in the YAML front matter. To regenerate the YAML block from the canonical DSFR sources, run `python3 scripts/build-decisions.py`.

> **Critical rule.** Don't apply Bleu France to non-interactive titles. The DSFR reserves it for *clickable* elements; using it on a heading creates ambiguity with links and buttons.

## Typography

### Faces

- **Marianne** (primary, sans-serif). The State's bespoke typeface. Use weights `light` (300), `regular` (400), `bold` (700), each with italics. **Fallback**: Arial.
- **Spectral** (secondary, serif). Weights `regular` (400) and `extra-bold` (800). Reserved for *secondary, minor, or distinguishing* text — applied via the `fr-text--alt` class. **Fallback**: Georgia.

> The DSFR explicitly recommends *not* using Spectral as the primary face. It's an accent.

### Titres (semantic headings)

The `h1`…`h6` typography tokens are applied to native `<h1>`–`<h6>` elements, or via the `fr-h1`…`fr-h6` utility class on any heading element. The breakpoint is **48em (768px)**: below it the tokens fall back to their `*-mobile` companions automatically (the `fr-h*` classes carry the `@media` rules — emit them rather than custom markup whenever possible).

All title levels share the same colour bindings: `{colors.text-title-grey}` on light backgrounds, inverted on dark (the dark mode of the same decision token already resolves to `#fff`). Margin-bottom is `{spacing.title-margin}` (24px) for every level.

| Niveau | Usages | Balise | Desktop (taille / line) | Mobile (taille / line) |
|--------|--------|--------|-------------------------|------------------------|
| **H1** | Titre principal de la page : il ne peut y en avoir qu'un par page. | `<h1>` | 40 / 48 px | 32 / 40 px |
| **H2** | Second niveau de titre de section ou de paragraphes. Leur nombre n'est pas limité. | `<h2>` | 32 / 40 px | 28 / 36 px |
| **H3** | Troisième niveau de sous-titre. Leur nombre n'est pas limité. | `<h3>` | 28 / 36 px | 24 / 32 px |
| **H4** | Quatrième niveau de sous-titre. Leur nombre n'est pas limité. | `<h4>` | 24 / 32 px | 22 / 28 px |
| **H5** | Cinquième niveau de sous-titre. Leur nombre n'est pas limité. | `<h5>` | 22 / 28 px | 20 / 28 px |
| **H6** | Sixième et plus petit niveau de sous-titre. Leur nombre n'est pas limité. | `<h6>` | 20 / 28 px | 18 / 24 px |

### Titres alternatifs (display sizes)

For editorial / hero / marketing surfaces the DSFR provides five oversized title styles. They are *not* semantic — apply them via the `fr-display--{size}` utility class on a heading element of the appropriate semantic level (most often an `<h1>`). All share `{colors.text-title-grey}` and a margin-bottom of `{spacing.display-margin}` (32px).

| Niveau | Classe | Desktop (taille / line) | Mobile (taille / line) |
|--------|--------|-------------------------|------------------------|
| **Titre alternatif XL** | `fr-display--xl` | 80 / 88 px | 72 / 80 px |
| **Titre alternatif LG** | `fr-display--lg` | 72 / 80 px | 64 / 72 px |
| **Titre alternatif MD** | `fr-display--md` | 64 / 72 px | 56 / 64 px |
| **Titre alternatif SM** | `fr-display--sm` | 56 / 64 px | 48 / 56 px |
| **Titre alternatif XS** | `fr-display--xs` | 48 / 56 px | 40 / 48 px |

### Body, lead, label

Body styles are size-stable across breakpoints (no mobile companions).

| Token | Class | Size / line | Weight | Use |
|-------|-------|-------------|--------|-----|
| `body-xl` | `fr-text--xl`, `fr-text--lead` | 1.25rem / 2rem (20 / 32 px) | 400 | Lead paragraph |
| `body-lg` | `fr-text--lg` | 1.125rem / 1.75rem (18 / 28 px) | 400 | Emphasised paragraph |
| `body-md` | `fr-text--md` | 1rem / 1.5rem (16 / 24 px) | 400 | Default body |
| `body-sm` | `fr-text--sm` | 0.875rem / 1.5rem (14 / 24 px) | 400 | Metadata, secondary |
| `body-xs` | `fr-text--xs` | 0.75rem / 1.25rem (12 / 20 px) | 400 | Captions, microcopy |
| `label` | — | 0.875rem / 1.5rem (14 / 24 px) | 700 | Form labels, button text |
| `body-md-alt` | `fr-text--alt` (+`fr-text--md`) | 1rem / 1.5rem (16 / 24 px) | 400 | Editorial Spectral pull-quote |
| `body-sm-alt` | `fr-text--alt` (+`fr-text--sm`) | 0.875rem / 1.5rem (14 / 24 px) | 400 | Spectral footnote / source |

### Rules

- Body line-height: `1.5rem` (1.5× on `body-md`) for comfortable long-form reading.
- Use sentence case for headings; reserve uppercase for utility microcopy with expanded letter-spacing (e.g. `fr-link--icon` labels).
- **Never** colour a title in Bleu France except via the `text-title-blue-france` decision token, which is reserved for explicit identity expressions.
- For all-caps utility microcopy, set letter-spacing `0.06em`.
- Prefer the `fr-h*` / `fr-display--*` utility classes over raw font-size declarations — they carry the responsive `@media` rules so mobile sizing happens automatically.

## Layout

### Container & grid

- **Max content width**: `78rem` (1248 px). Wider hero / footer surfaces extend full-bleed but content wraps to this max.
- **Grid**: 12 columns. Gutters: 16px mobile / 24px tablet / 32px desktop.
- **Side padding**: 24px mobile / 40px desktop.

### Breakpoints

| Name | Range |
|------|-------|
| `xs` | < 576 px |
| `sm` | ≥ 576 px |
| `md` | ≥ 768 px |
| `lg` | ≥ 992 px |
| `xl` | ≥ 1200 px |

The DSFR class system uses suffixed modifiers (`fr-grid-row--gutters`, `fr-col-md-6`) keyed on the breakpoints above.

### Spacing system

The DSFR is built on the **`v` unit**: `1v = 0.25rem = 4px`. The full ladder runs in single-`v` steps from `0v` to `32v` (with two fractional steps `0-5v` and `1-5v` for hairlines), and every step has a matching `fr-{prop}-Nv` utility class — `fr-mb-4v`, `fr-py-2v`, `fr-gap-6v`, `fr-mt-12v`, etc. The same scale governs both **horizontal** (margin/padding-left, gap-x) and **vertical** (margin/padding-top, gap-y) axes; the DSFR docs separate them visually but the tokens are shared.

The Figma library uses a parallel "**W** unit" where `1W = 2v = 8px`. The W naming surfaces in design specs and in the visual ladder below; the canonical implementation name is always `Nv`.

The most common stops, with their W aliases and typical use:

| Token | W | Value | Common use |
|-------|---|-------|------------|
| `1v`  | — | 4px   | Hairline spacing |
| `2v`  | `1W` | 8px | Tight inline gaps |
| `3v`  | — | 12px  | Compact stack |
| `4v`  | `2W` | 16px | **Default inter-component gap** (button group, form rows) |
| `6v`  | `3W` | 24px | Card / container padding, `title-margin` |
| `8v`  | `4W` | 32px | Section spacing, `display-margin` |
| `10v` | `5W` | 40px | Wide section gap |
| `12v` | `6W` | 48px | Large section gap |
| `14v` | `7W` | 56px | Page-level rhythm |
| `16v` | `8W` | 64px | Hero / page-level rhythm |
| `18v` | `9W` | 72px | Generous hero margin |
| `24v` | `12W` | 96px | Major editorial spacing |
| `30v` | `15W` | 120px | Maximum section break |

The DSFR also exposes a negative ladder (`n0-5v` … `n8v`) for negative margins, used sparingly — the YAML token block intentionally omits these; agents needing one should emit the corresponding `fr-m-nNv` class directly.

> **Whitespace philosophy.** Generous but utilitarian — *espace pour respirer*, not *espace pour épater*. The State is sober; the layout reflects that.

## Elevation & Depth

The DSFR is **flat by default**. Shadows are reserved for ephemeral surfaces and meaningful state changes:

| Token | Shadow | Use |
|-------|--------|-----|
| `e-0` | none | Default for cards, tiles, panels |
| `e-1` | `0 1px 2px rgba(0, 0, 18, 0.16)` | Subtle separation (rarely used) |
| `e-2` | `0 4px 8px rgba(0, 0, 18, 0.16)` | Modals, dialogs |
| `e-3` | `0 8px 16px rgba(0, 0, 18, 0.16)` | Dropdowns, popovers, on-hover lift for cards |

> **Focus ≠ shadow.** Visible focus is rendered as a **2px outer halo** in `focus-ring` (`#0a76f6`), drawn with `outline` rather than `box-shadow`. This is a hard accessibility requirement — never replace it with a shadow.

## Shapes

The DSFR has **no fundamentals-level border-radius spec**. Corners are square by convention — `rounded.none = 0` is the default for buttons, cards, modals, alerts, inputs, tiles, panels, and effectively everything else. Radius decisions live at the component level, where a small set of component-scoped exceptions are spelled out:

| Component | Radius | Token |
|-----------|--------|-------|
| Search input (top corners) | 4px | `rounded.sm` |
| Tags, badges | full | `rounded.pill` |
| Toggle switch knob/track | full | `rounded.pill` |

These three exceptions account for every non-zero radius in the DSFR. If you find yourself reaching for `rounded.sm` or `rounded.pill` on a component not listed above, you're out of step with the system.

> **Rationale.** Angularity reinforces officiality, restraint, and republican neutrality. Rounded corners would soften the visual register away from the State register the DSFR is designed to preserve.

## Components

Each component below is described once, then surfaced in the YAML token graph as `<component-name>` plus `<component-name>-<state>` entries. State variants follow the alpha `DESIGN.md` convention of separate component entries.

For each component, the **BEM class** column gives the canonical `fr-*` name an implementing agent should emit when generating real HTML — these classes pick up the JS behaviour shipped in `dsfr.module.min.js` automatically.

### Actions

#### Variants

The DSFR exposes four button variants. Each one has hover / active / disabled states; the disabled state collapses every variant to the same grey-on-grey rendering (`background-disabled-grey` / `text-disabled-grey`).

| Variant | BEM class | Visual |
|---------|-----------|--------|
| Primary | `.fr-btn` | `background-action-high-blue-france` fill, `text-inverted-blue-france` label, no border. |
| Secondary | `.fr-btn.fr-btn--secondary` | Transparent fill, blue label, 1 px `border-action-high-blue-france` outline. |
| Tertiary | `.fr-btn.fr-btn--tertiary` | Transparent fill, blue label, 1 px `border-default-grey` outline. |
| Tertiary, no outline | `.fr-btn.fr-btn--tertiary.fr-btn--no-outline` | Transparent fill, blue label, no border. Underlies the pre-baked icon buttons (see below). |

> **Implementation notes.**
>
> 1. **Borders.** The DSFR draws variant outlines with `box-shadow: inset 0 0 0 1px <color>`, not a real `border`, so the box does not gain 1 px of layout when the outline appears. The schema's component sub-tokens do not include `border`, so border colour is not encoded in the YAML — agents should emit the canonical `fr-*` classes (which set the right inset shadow) or apply the shadow themselves: `box-shadow: inset 0 0 0 1px {colors.border-action-high-blue-france}` for secondary, `{colors.border-default-grey}` for tertiary, and none for primary or tertiary-no-outline.
> 2. **Font weight.** All four variants render their label at `font-weight: 500` (500 = medium), one step heavier than the `body-md` default of 400. The schema does not surface font-weight as a component sub-token, so this lives in prose only.
> 3. **Disabled contrast.** Every `*-disabled` variant lands on `#929292` text over `#e5e5e5` background (2.47:1, below WCAG AA's 4.5:1 active-text minimum). This is intentional — WCAG 2.1 §1.4.3 exempts inactive controls from the contrast requirement, and the DSFR uses this exact pair throughout the system to mark disabled state distinctly.

#### Sizes

Three sizes; `md` is the default and is what the YAML's `button-primary` / `button-secondary` / `button-tertiary` entries describe. Sizes are deltas — `button-sm` and `button-lg` override only the dimensional properties and compose with any variant.

| Size | BEM modifier | min-height | padding | typography |
|------|--------------|------------|---------|------------|
| Small | `.fr-btn--sm` | 32 px | 4 px / 12 px | `body-sm` |
| Medium (default) | *(none)* | 40 px | 8 px / 16 px | `body-md` |
| Large | `.fr-btn--lg` | 48 px | 8 px / 24 px | `body-lg` |

#### Icons

Icon composition is markup-only — the same variant tokens apply, only the HTML changes. The DSFR uses `fr-btn--icon-left` / `fr-btn--icon-right` modifier classes plus an icon class (`fr-icon-*-line` or `fr-icon-*-fill`) to position a 16 px glyph next to the label.

```html
<!-- Icon on the left -->
<button class="fr-btn fr-btn--icon-left fr-icon-checkbox-line">Valider</button>

<!-- Icon on the right -->
<button class="fr-btn fr-btn--icon-right fr-icon-arrow-right-line">Continuer</button>

<!-- Icon only (square button — the label still exists for screen readers) -->
<button class="fr-btn fr-icon-close-line" title="Fermer">Fermer</button>
```

Rule: square icon-only buttons must keep an accessible label via `title=` or visually-hidden text; never strip the label from the markup.

#### Pre-baked icon buttons

The DSFR ships several convenience classes that compose `fr-btn--tertiary-no-outline` with a specific icon: `.fr-btn--close` (×), `.fr-btn--display` (theme switcher), `.fr-btn--team` (people), `.fr-btn--briefcase` (recruitment), `.fr-btn--account` (user), `.fr-btn--fullscreen`, `.fr-btn--tooltip`. They are not new design decisions — they are shorthands over `button-tertiary-no-outline` — and so are not enumerated in the YAML. Use them when the surface they appear on already requires that exact icon-and-tone combination (closing a modal, opening the display-mode panel, etc.).

#### Grouping

Group buttons with `.fr-btns-group` — vertical 2W (16 px) gap by default; `--inline` for horizontal at a breakpoint; `--equisized` to match all widths to the widest member.

### Forms

| Component | BEM class |
|-----------|-----------|
| Input (champ de saisie) | `.fr-input` (wrap in `.fr-input-group`; add `.fr-input-group--error` / `--valid` / `--disabled` for state) |
| Select (liste déroulante) | `.fr-select` |
| Checkbox (case à cocher) | `.fr-checkbox-group` + native `<input type="checkbox">` |
| Radio (bouton radio) | `.fr-radio-group` + native `<input type="radio">` |
| Toggle (interrupteur) | `.fr-toggle` |

Every form control must have a visible `<label>`; help and error messages live below the input as `.fr-hint-text`, `.fr-error-text`, or `.fr-valid-text`. The DSFR's *Champ de saisie* covers a fairly large surface (default text + 7 HTML input types + 4 composition patterns), so the rest of this section is dedicated to it.

#### Champ de saisie — states

| State | YAML entry | Underline (`box-shadow: inset 0 -2px 0 0 …`) | Label colour | Helper colour |
|-------|------------|--------------|--------------|---------------|
| Default | `input` | `{colors.border-plain-grey}` | `{colors.text-label-grey}` | `{colors.text-mention-grey}` (hint) |
| Focus | — *(uses global focus ring; no token override)* | unchanged | unchanged | unchanged |
| Error | `input-error` (group adds `.fr-input-group--error`) | `{colors.border-plain-error}` | `{colors.text-default-error}` | `{colors.text-default-error}` (`.fr-error-text`) |
| Success | `input-success` (group adds `.fr-input-group--valid`) | `{colors.border-plain-success}` | `{colors.text-default-success}` | `{colors.text-default-success}` (`.fr-valid-text`) |
| Disabled | `input-disabled` (group adds `.fr-input-group--disabled`) | `{colors.border-disabled-grey}` | `{colors.text-disabled-grey}` | `{colors.text-disabled-grey}` |

Three points the schema cannot express directly:

1. **Asymmetric corners.** The input rounds only its top corners (`border-radius: 0.25rem 0.25rem 0 0`). The YAML records `rounded: "{rounded.sm}"` because that is the closest single-value approximation; agents emitting `.fr-input` get the asymmetric form for free, anything custom should reproduce the half-rounding.
2. **Underline as box-shadow.** The 2 px bottom rule is drawn with `box-shadow: inset 0 -2px 0 0 <colour>`, not a real `border-bottom`, so the input's content area never shifts when the underline changes colour by state. The underline colour is the primary state signal — see the table above.
3. **Group-level error/success accent.** `.fr-input-group--error` and `--valid` add a 2 px coloured strip on the *left* of the whole group via a `::before` pseudo-element (offset −0.75 rem). It marks the entire field cluster (label + input + helper) as one validation unit.

#### Champ de saisie — HTML types

The `.fr-input` class applies the same tokens to every text-like form control. Switching `type=` only changes browser behaviour (keyboard, validation, native picker), never tokens. Stories on the DSFR demo page:

| `type` | Use case | Notes |
|--------|----------|-------|
| `text` (default) | Free text | — |
| `email` | E-mail | Native validation; `inputmode="email"` recommended |
| `tel` | Telephone | `inputmode="tel"` recommended; pair with hint *« Exemple : 0123456789 »* |
| `number` | Integer / decimal | Pair with hint *« Saisissez un nombre entier »* |
| `password` | Password | Native masking |
| `search` | Search query | Visually identical to `text`; the **search bar** component (`.fr-search-bar`) is a different composition that wraps an input + a primary button |
| `url` | URL | Pair with placeholder `https://` and hint *« Saisissez une url valide, commençant par https:// »* |
| `date` | Date | The DSFR injects a calendar SVG via `background-image` on the right (1 rem icon, 1 rem from the right edge) and reserves `padding-right: 3rem` so the native `::-webkit-calendar-picker-indicator` overlays it |

`<textarea>` reuses `.fr-input` directly (`textarea.fr-input`) and only changes `min-height` to `3.75rem` (60 px). All other tokens — colours, padding, underline, asymmetric corners — are identical.

#### Champ de saisie — composition

Four patterns from the DSFR demo page that combine `.fr-input` with surrounding markup. None of these introduce new tokens; they are layout/markup recipes.

**1. Hint text** — small caption between the label and the input.

```html
<div class="fr-input-group">
  <label class="fr-label" for="phone">Numéro de téléphone
    <span class="fr-hint-text">Exemple : 0123456789</span>
  </label>
  <input class="fr-input" type="tel" id="phone">
</div>
```

The hint text uses `text-mention-grey` and inherits `body-sm`. Place it inside the `<label>` so screen readers announce it as part of the field name.

**2. Trailing icon** — a 1 rem glyph anchored to the right of the input, used to surface a secondary signal (e.g. `fr-icon-warning-line` for a soft warning that does not warrant the full error state).

```html
<div class="fr-input-group">
  <label class="fr-label" for="city">Champ avec une icône</label>
  <div class="fr-input-wrap fr-icon-warning-line">
    <input class="fr-input" type="text" id="city">
  </div>
</div>
```

`.fr-input-wrap` is the positioning context; the icon is rendered via the `fr-icon-*` pseudo-element on the wrap, sized at 1 rem and offset 1 rem from the right edge. The input itself reserves no extra padding for it, so keep the icon purely decorative — never put critical information here.

**3. Combined with a button** (envoi or action) — input and button sit side-by-side inside `.fr-input-wrap--addon`. The input's underline switches to `border-action-high-blue-france` (blue) to signal the bound action, and the button squares to the input's height.

```html
<div class="fr-input-group">
  <label class="fr-label" for="newsletter">Champ avec bouton d'envoi associé</label>
  <div class="fr-input-wrap fr-input-wrap--addon">
    <input class="fr-input" type="email" id="newsletter">
    <button class="fr-btn">Envoyer</button>
  </div>
</div>
```

For the action variant, swap the `<button class="fr-btn">` for a `<button class="fr-btn fr-btn--tertiary fr-icon-delete-line">…</button>` — this composes the *Tertiary, no outline* button variant (already in the components YAML) with an icon.

**4. Date** — uses `<input type="date">` and lets the browser provide the popover. **The DSFR ships no datepicker JavaScript**; the calendar UI that opens on click is whatever the browser provides natively (Chrome, Edge, Safari, and Firefox each have their own interface, with their own translations and locale rules). The design system stylises only the *field* — same surface, same underline, plus an SVG calendar icon overlaid on the right via `background-image`, scoped to browsers that expose `::-webkit-calendar-picker-indicator` (Chromium + Safari). The browser's default indicator is hidden (`opacity: 0`) but kept as the click target so the popover still opens. Firefox falls back to its native rendering, which differs visually but works the same.

This is a deliberate trade-off: the field is consistent across browsers, the popover is not. Pair `<input type="date">` with a hint text giving the expected format (e.g. *« Format : jj/mm/aaaa »*) because some browsers do not render the placeholder for `type="date"` inputs.

```html
<div class="fr-input-group">
  <label class="fr-label" for="dob">Date simple
    <span class="fr-hint-text">Format : jj/mm/aaaa</span>
  </label>
  <input class="fr-input" type="date" id="dob">
</div>
```

#### Liste déroulante

The select reuses every convention from the input — same surface tokens, same asymmetric corners, same `box-shadow: inset 0 -2px 0 0 <colour>` underline, same group-level `::before` accent strip, same hint-text and helper-text patterns. The state mapping is identical too:

| State | YAML entry | Underline colour | Group modifier |
|-------|------------|------------------|----------------|
| Default | `select` | `{colors.border-plain-grey}` | — |
| Focus | — *(global focus ring)* | unchanged | — |
| Error | `select-error` | `{colors.border-plain-error}` | `.fr-select-group--error` |
| Success | `select-success` | `{colors.border-plain-success}` | `.fr-select-group--valid` |
| Disabled | `select-disabled` | `{colors.border-disabled-grey}` | `.fr-select-group--disabled` |

The two select-specific differences:

1. **Chevron icon.** A 1 rem chevron-down SVG is drawn on the right via `background-image` (light fill `#161616` / dark fill `#fff`), anchored 1 rem from the right edge — same technique as the date input. Right padding is bumped to `2.5 rem` to keep the option text from running under the icon. The browser's default `<select>` arrow is suppressed via `appearance: none`.

2. **No `<input type=…>` axis.** A `<select>` is a single element — no twelve-way HTML-type axis to document. Composition is also narrower: hint text is the only common pattern. Inputs combined with a button use `.fr-input-wrap--addon`; selects do not have an equivalent addon recipe in the canonical CSS (use a separate `.fr-btn` placed beside the field via the grid).

```html
<!-- Default + hint -->
<div class="fr-select-group">
  <label class="fr-label" for="region">Libellé de la liste déroulante
    <span class="fr-hint-text">Texte de description additionnel</span>
  </label>
  <select class="fr-select" id="region">
    <option value="" disabled selected hidden>Sélectionnez une option</option>
    <option>Île-de-France</option>
    <option>Bretagne</option>
    <option>Occitanie</option>
  </select>
</div>

<!-- Error -->
<div class="fr-select-group fr-select-group--error">
  <label class="fr-label" for="region">Libellé de la liste déroulante</label>
  <select class="fr-select" id="region" aria-describedby="region-error">…</select>
  <p id="region-error" class="fr-error-text">Sélectionnez une option valide</p>
</div>
```

#### Case à cocher

The checkbox is a multi-axis component. Standalone, it carries `checkbox` (default 24 px) and `checkbox-sm` (16 px) tokens; checked state swaps the fill to `background-active-blue-france` and overlays a white check SVG (light) / blue check SVG (dark). The box itself uses `rounded.sm` (`0.25 rem`) and a 1 px outline drawn from `border-action-high-blue-france`. Disabled state replaces both fill and outline with `background-disabled-grey` and dims the label to `text-disabled-grey`.

Most production usage wraps multiple checkboxes inside a `<fieldset class="fr-fieldset">` with a `<legend class="fr-fieldset__legend">`. The fieldset adds the *group* axis:

| Group state | YAML entry (label) | Modifier | Visual |
|-------------|--------------------|----------|--------|
| Default | — *(`checkbox` only)* | — | Black legend, default labels |
| Hint | — | `<legend>` includes `.fr-hint-text` | Hint paragraph under legend |
| Hint per item | — | each `<label>` includes `.fr-hint-text` | Hint paragraph under each box |
| Inline | — | `.fr-fieldset--inline` | Boxes laid out horizontally |
| Disabled | `checkbox-disabled` | `<fieldset disabled>` | Greyed-out legend + boxes |
| Error | `checkbox-error` | `.fr-fieldset--error` | Red legend + 2 px red strip on left + `.fr-error-text` |
| Success | `checkbox-success` | `.fr-fieldset--valid` | Green legend + 2 px green strip on left + `.fr-valid-text` |

Two notes:

1. **The boxes themselves do not change colour for error/success states** — only the surrounding legend, labels, and the 2 px left strip change. This mirrors the `.fr-fieldset` accent used by all other group-able form controls (radios, date-fields).

2. **The fieldset's left strip is `position: absolute; left: -0.75 rem`** in the canonical CSS — it visually escapes the fieldset's content area to align with the form field's natural left edge. In our preview we collapse this into a 2 px `::before` inside the fieldset's left padding for simplicity; the visual is identical.

```html
<!-- Default group -->
<fieldset class="fr-fieldset">
  <legend class="fr-fieldset__legend">Légende pour l'ensemble des éléments</legend>
  <div class="fr-fieldset__element">
    <div class="fr-checkbox-group">
      <input type="checkbox" id="cb-1">
      <label class="fr-label" for="cb-1">Checkbox 1</label>
    </div>
  </div>
  <!-- … -->
</fieldset>

<!-- Error group with hint per item -->
<fieldset class="fr-fieldset fr-fieldset--error" aria-labelledby="cb-legend cb-error">
  <legend class="fr-fieldset__legend" id="cb-legend">Légende pour l'ensemble des éléments</legend>
  <div class="fr-fieldset__element">
    <div class="fr-checkbox-group">
      <input type="checkbox" id="cb-1">
      <label class="fr-label" for="cb-1">Checkbox 1
        <span class="fr-hint-text">Texte additionnel</span>
      </label>
    </div>
  </div>
  <div class="fr-messages-group" id="cb-error">
    <p class="fr-message fr-message--error">Texte d'erreur</p>
  </div>
</fieldset>
```

#### Bouton radio

The radio button mirrors the checkbox structurally: same `<fieldset>/<legend>` group composition, same `--inline` modifier, same hint patterns, same disabled / error / success group states with the 2 px left strip. Differences are purely visual:

1. **Pill-shaped, not square.** `rounded.pill` instead of `rounded.sm`. Default size is still 24 px (`md`); sm is 16 px.
2. **Checked indicator is an inner dot, not a check SVG.** Canon stacks two radial gradients: the outer ring (transparent core, blue ring at 11–12 px), and the inner dot (blue fill at 5–6 px). In our preview we use a single `radial-gradient(circle at center, blue 0 32%, white 40%)` to fake the same visual.
3. **Inner dot stays blue in error/success groups.** Only the *ring* changes colour — canon achieves this by re-emitting the outer radial-gradient with `border-plain-error` / `border-plain-success` while leaving the dot's gradient unchanged. Functionally equivalent: red/green ring around a blue dot.

| Group state | YAML entry | Modifier | Visual |
|-------------|------------|----------|--------|
| Default | — *(`radio` only)* | — | Black legend + black labels + blue ring |
| Hint | — | `<legend>` + `.fr-hint-text` | Hint paragraph under legend |
| Hint per item | — | each `<label>` + `.fr-hint-text` | Hint paragraph under each radio |
| Inline | — | `.fr-fieldset--inline` | Radios laid out horizontally |
| Disabled | `radio-disabled` | `<fieldset disabled>` | Greyed legend + greyed rings |
| Error | `radio-error` | `.fr-fieldset--error` | Red legend, red ring, blue dot, 2 px red strip on left |
| Success | `radio-success` | `.fr-fieldset--valid` | Green legend, green ring, blue dot, 2 px green strip on left |

##### Bouton radio riche (`fr-radio-rich`)

A composition pattern unique to radio. The radio is wrapped in a tile-like container that includes:
- A 5.5 rem × 5.5 rem **pictogram cell** on the side (canon defaults to flush-left; an `--align-right` variant flips it).
- A **title + optional hint** stack in the body.
- The actual radio circle anchored to the top-right of the tile.

Selection lights up the entire tile border in `border-action-high-blue-france` (canon adds an inset 1 px shadow to keep the border weight stable while the colour transitions). Hover and active states tint the body and pictogram cells via `background-default-grey-hover` / `-active`.

```html
<!-- Default radio group -->
<fieldset class="fr-fieldset">
  <legend class="fr-fieldset__legend">Légende pour l'ensemble des éléments</legend>
  <div class="fr-fieldset__element">
    <div class="fr-radio-group">
      <input type="radio" id="r-1" name="r"><label class="fr-label" for="r-1">Radio 1</label>
    </div>
  </div>
  <!-- … -->
</fieldset>

<!-- Bouton radio riche -->
<div class="fr-radio-group fr-radio-rich">
  <input type="radio" id="rr-1" name="rr">
  <label class="fr-label" for="rr-1">Titre
    <span class="fr-hint-text">Description courte</span>
  </label>
  <div class="fr-radio-rich__pictogram">
    <svg class="fr-artwork" aria-hidden="true" viewBox="0 0 80 80">…</svg>
  </div>
</div>
```

#### Interrupteur

The toggle (`fr-toggle`) is structurally a `<input type="checkbox">` rendered as a 40 × 24 px sliding pill. Three details set it apart from the other form controls:

1. **OFF state is stroked, not filled.** The track in OFF state is a *white interior* with a 1 px `border-action-high-blue-france` outline — turning it ON fills the track with `text-action-high-blue-france` and reveals a small blue check ✓ inside the still-white thumb. The thumb keeps its 1 px blue-france ring at all times.
2. **Optional microstate label.** A small "Activé" / "Désactivé" caption can render *below* the track in `text-active-blue-france` — exposed via the `data-fr-checked-label` / `data-fr-unchecked-label` attributes on the `<label>` and rendered through `::before` in canon. Useful for longer-form toggles where a screen-only state caption helps clarity.
3. **Border-bottom modifier.** `.fr-toggle--border-bottom` adds a single 1 px `border-default-grey` rule under the toggle row — used to visually separate stacked toggles in a fieldset (the *Border Group Story*).

| Story | YAML entry | Modifier | Visual |
|-------|------------|----------|--------|
| Default (off) | `toggle` | — | White track, blue stroke, white thumb left |
| Activé (on) | `toggle-on` | `<input>:checked` | Blue track, white thumb right with blue ✓ |
| Description | — | `+ .fr-hint-text` | Hint paragraph below toggle row |
| Microstate | `toggle-state` | label has `data-fr-{un,}checked-label` | "Activé" / "Désactivé" caption below track |
| Disabled | `toggle-disabled` | `<input>:disabled` | Grey track stroke, grey thumb ring, grey label |
| Error (group) | `toggle-error` | `.fr-fieldset--error` (or `.fr-toggle--error`) | Red label, 2 px red strip on left, helper text |
| Success (group) | `toggle-success` | `.fr-fieldset--valid` | Green label, 2 px green strip on left, helper text |
| Border-bottom | — | `.fr-toggle--border-bottom` | 1 px bottom rule under each toggle |

The ON state's track fill stays blue even inside an error or success group — only the *label* and the *strip* take the state colour. This mirrors the radio's blue inner dot.

```html
<!-- Default toggle -->
<div class="fr-toggle">
  <input type="checkbox" class="fr-toggle__input" id="t-1">
  <label class="fr-toggle__label" for="t-1">Libellé de l'interrupteur</label>
</div>

<!-- With microstate caption + hint -->
<div class="fr-toggle">
  <input type="checkbox" class="fr-toggle__input" id="t-2">
  <label class="fr-toggle__label" for="t-2"
         data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">
    Libellé de l'interrupteur
  </label>
  <span class="fr-hint-text">Texte additionnel</span>
</div>

<!-- Border group: stack with separators -->
<fieldset class="fr-fieldset">
  <legend class="fr-fieldset__legend">Légende pour l'ensemble des éléments</legend>
  <div class="fr-fieldset__element">
    <div class="fr-toggle fr-toggle--border-bottom">
      <input type="checkbox" id="t-g-1"><label for="t-g-1">Libellé 1</label>
    </div>
  </div>
  <!-- … -->
</fieldset>
```

### Surfaces

| Component | BEM class |
|-----------|-----------|
| Card (carte) | `.fr-card` (`--horizontal` for side-by-side image; `--no-arrow` to hide the action chevron) |
| Tile (tuile) | `.fr-tile` (smaller, denser variant of card; primary content is a single link) |
| Callout (mise en avant) | `.fr-callout` |

Cards are flat at rest; on `:hover` they may apply `e-3` to suggest interactivity if the entire card is a link.

#### Carte

The card has three sizes that modulate **body padding** and **title size** while keeping the same overall structure (image / title / optional description / arrow). The `--md` modifier exists in the canon but is a no-op vs default, so practical usage is `--sm`, default, `--lg`.

| Story | Modifier | Body padding | Title (size / line-height) | Description size | Arrow icon |
|-------|----------|--------------|----------------------------|------------------|-----------|
| Default | *(none)* | `2rem` (32 px) | `1.25rem / 1.75rem` (20 / 28) | `0.875rem / 1.5rem` | 1 rem |
| Sm | `.fr-card--sm` | `1.5rem` (24 px) | `1.125rem / 1.5rem` (18 / 24) | same | 1 rem |
| Md | `.fr-card--md` | `2rem` (= default) | `1.25rem / 1.75rem` (= default) | same | 1 rem |
| Lg | `.fr-card--lg` | `2.5rem` (40 px) | `1.375rem / 1.75rem` (22 / 28) | `1rem / 1.5rem` | 1.5 rem |

Three visual constants across all sizes:

- **Title** is rendered in `text-title-blue-france` with weight 700; the trailing `→` arrow is anchored to the bottom-right of the body via the `__end` slot in canon, drawn from the `arrow-right-line.svg` system icon at 1 rem (1.5 rem in `--lg`).
- **Image** uses an aspect ratio of ~16/10 in the canonical demos. The image element itself is structurally `.fr-card__img > img` and has no token styling beyond `object-fit: cover`. The placeholder asset is the same lavender mountain SVG across all sizes — the size modifiers do not change the image styling.
- **Border** is 1 px `border-default-grey` unless `.fr-card--no-border` or `.fr-card--shadow` is set.

**Hover & active states.** When the entire card is interactive (`.fr-enlarge-link` or `.fr-enlarge-button` — the most common preset), hovering darkens the image via a `filter: brightness()` (canon decrements 10 % in light theme, increments 10 % in dark theme — a unified "darken" perception thanks to the `--brighten` direction-aware variable), and tints the card body background to `background-default-grey-hover`. Active state pushes the same delta to 20 %. The two effects together produce a clearly perceptible interactivity feedback: the image area appears to gain a grey overlay, and the body background shifts from white to a faint warm grey.

**Layout axis.** Above the `md` breakpoint the card switches from a top-image vertical stack to a side-by-side row when one of three modifiers is set. The image region width is fixed; everything else flows into the remaining track.

| Modifier | Image width | Body width |
|----------|-------------|------------|
| *(none)* | 100 % (top) | 100 % (below image) |
| `.fr-card--horizontal` | 40 % (left) | 60 % (right) |
| `.fr-card--horizontal-half` | 50 % | 50 % |
| `.fr-card--horizontal-tier` | 33.3 % | 66.7 % |

Below the `md` breakpoint, all three horizontal modifiers collapse back to the vertical stack — the canonical CSS guards the `flex-direction: row` behind a `min-width` media query so the layout responds gracefully on mobile.

**Decoration axis.** Background colour, border, and elevation are toggled independently:

| Modifier | Background | Border | Elevation |
|----------|------------|--------|-----------|
| *(none)* | `background-default-grey` (white) | 1 px `border-default-grey` | flat |
| `.fr-card--grey` | `background-contrast-grey` (light grey) | 1 px border | flat |
| `.fr-card--shadow` | `background-raised-grey` | none | `drop-shadow(--raised-shadow)` |
| `.fr-card--shadow.fr-card--grey` | `background-contrast-raised-grey` | none | `drop-shadow` |
| `.fr-card--no-border` | `background-default-grey` | none | flat |
| `.fr-card--no-background` | `transparent` | 1 px border | flat |

The border-vs-shadow split is handled by the canonical selector `.fr-card:not(.fr-card--no-border):not(.fr-card--shadow)` — adding either modifier removes the inset gradient that draws the four 1 px sides.

**Slots & composition.** Inside `__content` the canonical card lays out three optional regions plus the title and description:

| Slot | BEM | Typical content |
|------|-----|-----------------|
| Start | `.fr-card__start` | `fr-badges-group`, `fr-tags-group`, `fr-card__detail` (small descriptor in `text-mention-grey`, body-xs, sits above the title) |
| Title + desc | `.fr-card__title`, `.fr-card__desc` | The card's main reading content |
| End | `.fr-card__end` | Detail tail (date, author), the trailing arrow icon when `enlarge-link` |
| Footer | `.fr-card__footer` | Standalone action buttons, secondary links — sits below the body and outside the enlarged hit-area |

`fr-badges-group` placed in `__header` instead of `__start` floats the badges over the top-left of the image (used in news-item cards). `__detail` is a single-line caption — typically a date or category — that scoots up to sit just above the title with `margin-bottom: -1rem` (canon).

**Action variants.** The trailing icon and the click target both depend on three independent flags:

| Modifier | Icon | Click target | Use case |
|----------|------|--------------|----------|
| `.fr-enlarge-link` *(default in canon demos)* | arrow-right (`→`) | entire card | Card linking to a page |
| `.fr-enlarge-button` | arrow-right | entire card (button) | Card triggering an action (modal, expand) |
| `.fr-card--download` | download (`↓`) | entire card | File card — title becomes a download link, body shows file metadata via `__detail` |
| `.fr-card--no-arrow` | *(none)* | depends on link/button modifier | Decorative or contextual card without explicit affordance |
| `.fr-card--no-icon` | *(none)* | depends on link/button modifier | Same as `--no-arrow`, kept for legacy markup |

`.fr-card--download` also overrides the layout to row (image left at 40 %), and constrains its `__img` to `object-fit: contain` over a `background-alt-grey` panel — file thumbnails are shown padded inside their tile rather than cropped to fill.

```html
<div class="fr-card fr-enlarge-link fr-card--lg">
  <div class="fr-card__body">
    <div class="fr-card__content">
      <h3 class="fr-card__title"><a href="…">Intitulé de la carte</a></h3>
      <p class="fr-card__desc">Description optionnelle.</p>
    </div>
  </div>
  <div class="fr-card__header">
    <div class="fr-card__img">
      <img src="…" alt="">
    </div>
  </div>
</div>
```

#### Tuile

The tile (`fr-tile`) is the card's denser sibling. It carries a **pictogram** (an SVG illustration sized 5 rem × 5 rem) instead of a hero image, and is decorated by a **4 px coloured rule on its bottom edge** that signals interactivity. Unlike the card, the tile only ships in two sizes (default and `--sm`).

**Sizes.**

| Story | Modifier | Padding | Title | Pictogram | Detail |
|-------|----------|---------|-------|-----------|--------|
| Default | *(none)* | `2rem 2rem 2.25rem` (32 / 32 / 36) | `1.125rem / 1.5rem` (18 / 24) | 5 rem × 5 rem | `0.75rem / 1.25rem` |
| Sm | `.fr-tile--sm` | `1.5rem 1.5rem 1.75rem` (24 / 24 / 28) | `1rem / 1.5rem` (16 / 24) | 3.5 rem × 3.5 rem | same |
| Horizontal | `.fr-tile--horizontal` | same as default | same | 4 rem × 4 rem | margin-bottom: -2.5 rem |
| Sm + Horizontal | combo | sm padding | sm title | 2.5 rem × 2.5 rem | sm spacing |

**The bottom rule.** Drawn via a `linear-gradient` background on `__title::before` (4 px high, full-width). Two colours:

| Variant | Title element | Rule colour | Title text colour |
|---------|---------------|-------------|-------------------|
| Interactive | `__title > a` or `__title > button` | `border-active-blue-france` (`#000091` / `#8585f6`) | `text-action-high-blue-france` |
| Static / no-link | `__title` (text only, no nested anchor) | `border-plain-grey` (`#3a3a3a` / `#cecece`) | `text-title-grey` |

This is the tile's most distinctive token: it is the only common surface in DSFR where the bottom 4 px is a coloured rule, and the colour carries semantic weight (blue = clickable, dark grey = decorative).

**Layout axis.** Vertical (default — pictogram on top, content centred) vs horizontal (pictogram left, content right, text left-aligned). The horizontal modifier reduces the pictogram to 4 rem so the row stays compact. A responsive variant `.fr-tile--horizontal.fr-tile--vertical@md` (and `@lg`) starts horizontal and switches to vertical above the breakpoint — useful for grids that flow from compact list-style on mobile to picto-on-top above the fold on desktop.

**Decoration axis.** Identical mechanism to the card — same 5 modifiers, same colour pairs:

| Modifier | Background |
|----------|------------|
| *(none)* | `background-default-grey` (white) |
| `.fr-tile--grey` | `background-contrast-grey` |
| `.fr-tile--shadow` | `background-raised-grey` + drop-shadow, no border |
| `.fr-tile--shadow.fr-tile--grey` | `background-contrast-raised-grey` + drop-shadow |
| `.fr-tile--no-border` | white, no border |
| `.fr-tile--no-background` | transparent |

By DSFR convention, **tiles carrying a `__start` badge** are typically paired with `--grey` (the badge sits more clearly on the tinted body). Tiles with a `__start` tag use the default white background.

**Slots & composition.**

| Slot | BEM | Order | Typical content |
|------|-----|-------|-----------------|
| Header | `.fr-tile__header` | 1 (top) | `.fr-tile__pictogram > svg` |
| Start | `.fr-tile__start` (inside `__body`) | 1 (above title) | `fr-badges-group`, `fr-tags-group` |
| Body | `.fr-tile__body > __title + __desc + __detail` | 2 | Title (h3 wrapping `<a>`), description, detail |
| Detail | `.fr-tile__detail` | 4 (bottom of body) | Caption — date, file metadata (Extension - Poids - Langue), author |

**Action variants.**

| Modifier | Trailing icon | Title element | Rule colour | Use case |
|----------|---------------|---------------|-------------|----------|
| `.fr-enlarge-link` *(default in canon demos)* | `→` (1.5 rem; 1 rem in `--sm`) | `<a>` inside title | blue | Tile linking to a page |
| `.fr-enlarge-button` | `→` | `<button>` inside title | blue | Tile triggering an action |
| `.fr-tile--download` | `↓` (download-line.svg) | `<a>` (download attribute) | blue | File tile — `__detail` carries Extension / Weight / Language |
| `.fr-tile--no-icon` | *(none)* | `<a>`/`<button>` | blue | Decorative tile without explicit affordance |
| *no nested link* | *(none)* | text only | grey | Static informational tile (DSFR's "No Link Story") |

The `--download` modifier also forces horizontal layout (`flex-direction: row`) and overrides the trailing icon to the download glyph. When stacked with `--sm` it produces the canon's "Download Sm" preset.

```html
<!-- Default tile -->
<div class="fr-tile fr-enlarge-link">
  <div class="fr-tile__body">
    <div class="fr-tile__content">
      <h3 class="fr-tile__title"><a href="…">Intitulé de la tuile</a></h3>
      <p class="fr-tile__desc">Description (optionnelle)</p>
      <p class="fr-tile__detail">Détail (optionnel)</p>
    </div>
  </div>
  <div class="fr-tile__header">
    <div class="fr-tile__pictogram">
      <svg class="fr-artwork" aria-hidden="true" viewBox="0 0 80 80">…</svg>
    </div>
  </div>
</div>

<!-- Download tile -->
<div class="fr-tile fr-tile--download fr-enlarge-link">
  <div class="fr-tile__body">
    <div class="fr-tile__content">
      <h3 class="fr-tile__title"><a download href="…">Télécharger le document XX</a></h3>
      <p class="fr-tile__detail">PDF — 1,2 Mo — Français</p>
    </div>
  </div>
  <div class="fr-tile__header">
    <div class="fr-tile__pictogram">…</div>
  </div>
</div>
```

#### Mise en avant

The callout (`fr-callout`) is a grey-tinted block with a **4 px coloured rule on its left edge**, used to highlight a notice, summarise key information, or pair an action with a contextual prompt. Structurally simpler than card and tile — no image, no pictogram, just three optional slots inside a tinted body.

**Anatomy.**

| Element | BEM | Typography | Colour |
|---------|-----|------------|--------|
| Body (background) | `.fr-callout` | — | `background-contrast-grey` |
| Left rule (4 px) | drawn via `linear-gradient` background-image | — | `border-default-blue-france` (default) or thematic |
| Icon *(optional)* | `fr-icon-*` class on `.fr-callout` itself, rendered via `::before` | 1 rem icon mask | `text-title-grey` |
| Title | `.fr-callout__title` | h4 — `1.375rem / 1.75rem`, weight 700 | `text-title-grey` |
| Text | `.fr-callout__text` | body-lg — `1.125rem / 1.75rem` | `text-default-grey` |
| Action *(optional)* | `.fr-btn` (any standard button variant) | — | inherits button tokens |

Padding is `1.5rem` on all four sides; default block margin is `0 0 1.5rem`. The icon, when present, sits **above** the title (`display: block; margin: -0.5rem 0 0.5rem`) — it's not a left-side decorator but a stacked tag.

**Composition matrix.** The 4 DSFR demo stories (Default / Icon / Button / Icon+Button) are all permutations of two binary slots:

| Slot | Toggle | Effect |
|------|--------|--------|
| Icon | Add `fr-icon-information-line` (or any `fr-icon-*` class) directly on `.fr-callout` | Icon block appears above the title |
| Button | Add `<button class="fr-btn">…</button>` (or `<a class="fr-btn">`) inside the callout | Button appears below the text with `margin-top: 1rem` |

The Icon+Button story is just `icon=on, button=on` — no extra rule.

**Thematic colour variants.** The callout supports a 17-element thematic palette via single-class modifiers `fr-callout--<name>`. Each variant swaps **both** the body background (`background-contrast-{name}`) and the left rule (`border-default-{name}`) to a coordinated colour pair, while leaving title, text, and icon colours unchanged (so contrast remains readable across themes).

| Variant | BG (light) | Rule (light) | Use |
|---------|------------|--------------|-----|
| *(default)* | `background-contrast-grey` (`#eeeeee`) | `border-default-blue-france` (`#000091`) | Generic notice |
| `--green-tilleul-verveine` | tilleul tinted bg | green rule | Sustainability, ecology |
| `--green-bourgeon` | bourgeon tinted bg | green rule | Plant / agriculture |
| `--green-emeraude` | emeraude tinted bg | green rule | Health |
| `--green-menthe` | menthe tinted bg | green rule | Education |
| `--green-archipel` | archipel tinted bg | green rule | Maritime / overseas |
| `--blue-ecume` | écume tinted bg | blue rule | Defence / sea |
| `--blue-cumulus` | cumulus tinted bg | blue rule | Sport / weather |
| `--purple-glycine` | glycine tinted bg | purple rule | Culture |
| `--pink-macaron` | macaron tinted bg | pink rule | Tourism |
| `--pink-tuile` | tuile tinted bg (`#fee9e7`) | terracotta rule (`#ce614a`) | DSFR's "Accent" preset |
| `--yellow-tournesol` | tournesol tinted bg | yellow rule | Energy |
| `--yellow-moutarde` | moutarde tinted bg | mustard rule | Justice / regulation |
| `--orange-terre-battue` | terre-battue tinted bg | orange rule | Industry |
| `--brown-cafe-creme` | café-crème tinted bg | brown rule | Heritage |
| `--brown-caramel` | caramel tinted bg | caramel rule | Local government |
| `--brown-opera` | opéra tinted bg | brown rule | Generic warm accent |
| `--beige-gris-galet` | beige tinted bg | beige rule | Generic neutral accent |

The thematic colour names map to French ministerial / administrative palettes — agencies typically pick the variant aligned with their branding. From a CSS perspective they are all generated by the same template: each variant rule is exactly two background-* property assignments. The light/dark theme system handles the corresponding dark-mode tokens automatically.

```html
<!-- Default callout, no icon, no button -->
<div class="fr-callout">
  <h3 class="fr-callout__title">Titre de la mise en avant</h3>
  <p class="fr-callout__text">Lorem ipsum dolor sit amet, consectetur adipiscing.</p>
</div>

<!-- With icon and button -->
<div class="fr-callout fr-icon-information-line">
  <h3 class="fr-callout__title">Information</h3>
  <p class="fr-callout__text">Texte d'explication.</p>
  <button class="fr-btn">En savoir plus</button>
</div>

<!-- Thematic accent -->
<div class="fr-callout fr-callout--pink-tuile">
  <h3 class="fr-callout__title">Mise en avant accent</h3>
  <p class="fr-callout__text">Texte d'explication.</p>
</div>
```

### Tags & badges

| Component | BEM class |
|-----------|-----------|
| Tag | `.fr-tag` (sizes `--sm`, default; can be `<a>` or `<button>` for selectable) |
| Badge | `.fr-badge` (variants `--success`, `--warning`, `--error`, `--info`, `--new`) |

Tags and badges are the **only** components that use `rounded.pill`.

### Feedback

| Component | BEM class |
|-----------|-----------|
| Alert | `.fr-alert` + `.fr-alert--success | --warning | --error | --info`; size suffixes `--sm` |
| Notice (bandeau d'information) | `.fr-notice` |

Alerts include a leading icon (info/check/exclamation/cross) and an optional close button (`.fr-btn--close`).

### Navigation & branding

| Component | BEM class |
|-----------|-----------|
| Breadcrumb (fil d'Ariane) | `.fr-breadcrumb` |
| Modal (modale) | `.fr-modal` (focus trap + scroll lock provided by the JS) |
| Header (en-tête) | `.fr-header` (includes `.fr-header__brand`, `.fr-header__service`, `.fr-header__tools`) |
| Footer (pied de page) | `.fr-footer` (includes `.fr-footer__brand`, `.fr-footer__bottom`, `.fr-footer__partners`) |

The header is the brand carrier: the Marianne lockup (*"République Française"*) sits in `.fr-header__brand`, and the operator/service lockup sits beside it in `.fr-header__service`. This is the canonical *bloc marque* and must be present on every State page.

## Do's and Don'ts

### ✅ Do

- Reference **decision tokens** (`text-action-high-blue-france`, `background-default-grey`, `border-default-grey`) in components — never option tokens directly.
- Pair every interactive element with a **visible focus state** drawn with `focus-ring` as an outline.
- Use **`data-fr-scheme`** for theme switching; never hard-code colours per theme.
- Keep **touch targets ≥ 44×44 px** (button `--sm` is 32 px tall but its hit-area is padded to compensate).
- Choose **one illustrative family per page** when accenting editorial content.
- Use Marianne as the workhorse face; reserve Spectral (`fr-text--alt`) for secondary or distinguishing text.
- Lint the `DESIGN.md` against the Stitch CLI before publishing changes (`npx @google/design.md lint DESIGN.md`).

### ❌ Don't

- **Don't** apply Bleu France to titles or to any non-interactive text — it's reserved for actions.
- **Don't** introduce border-radius on buttons, cards, modals, alerts. Square corners are intentional.
- **Don't** mix light-theme and dark-theme tokens in the same context.
- **Don't** use the Marianne logo, the *République Française* lockup, or Bleu France as a brand mark outside an authorised .gouv.fr context.
- **Don't** add resting-state shadows to plain cards — reserve elevation for menus, modals, and hover lift.
- **Don't** use the illustrative palette for actions or system states.
- **Don't** treat Rouge Marianne as a destructive-action red — use the `error` token (`#ce0500`).
- **Don't** colour a heading with `primary` even if it looks attractive — accessibility audits and DSFR conformance both flag it.

---

> **References used to build this file.**
> DSFR documentation — <https://www.systeme-de-design.gouv.fr> ·
> DSFR source — <https://github.com/GouvernementFR/dsfr> ·
> `DESIGN.md` spec — <https://github.com/google-labs-code/design.md>.
