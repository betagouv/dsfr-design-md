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
  grey-950-150:                   "#eeeeee"
  grey-950-150-hover:             "#d2d2d2"
  grey-950-150-active:            "#c1c1c1"
  # Canonical decision-token target for `background-contrast-grey`.
  grey-950-100:                   "#eeeeee"
  grey-950-100-hover:             "#d2d2d2"
  grey-950-100-active:            "#c1c1c1"
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
  background-action-high-blue-france:        "{colors.blue-france-sun-113-625}"   # used 41×
  background-action-high-blue-france-active: "{colors.blue-france-sun-113-625-active}"   # used 3×
  background-action-high-blue-france-hover:  "{colors.blue-france-sun-113-625-hover}"   # used 3×
  background-action-high-error:              "{colors.error-425-625}"   # used 2×
  background-action-high-error-active:       "{colors.error-425-625-active}"   # used 2×
  background-action-high-error-hover:        "{colors.error-425-625-hover}"   # used 2×
  background-action-high-grey:               "{colors.grey-200-850}"   # used 2×
  background-action-high-grey-active:        "{colors.grey-200-850-active}"   # used 2×
  background-action-high-grey-hover:         "{colors.grey-200-850-hover}"   # used 2×
  background-action-low-blue-france:         "{colors.blue-france-925-125}"   # used 5×
  background-action-low-blue-france-active:  "{colors.blue-france-925-125-active}"   # used 3×
  background-action-low-blue-france-hover:   "{colors.blue-france-925-125-hover}"   # used 3×
  background-active-blue-france:             "{colors.blue-france-sun-113-625}"   # used 23×
  background-active-blue-france-active:      "{colors.blue-france-sun-113-625-active}"   # used 7×
  background-active-blue-france-hover:       "{colors.blue-france-sun-113-625-hover}"   # used 7×
  background-alt-grey:                       "{colors.grey-975-75}"   # used 6×
  background-alt-grey-active:                "{colors.grey-975-75-active}"   # used 6×
  background-alt-grey-hover:                 "{colors.grey-975-75-hover}"   # used 6×
  background-contrast-error:                 "{colors.error-950-100}"   # used 2×
  background-contrast-error-active:          "{colors.error-950-100-active}"   # used 2×
  background-contrast-error-hover:           "{colors.error-950-100-hover}"   # used 2×
  background-contrast-grey:                  "{colors.grey-950-100}"   # used 13×
  background-contrast-grey-active:           "{colors.grey-950-100-active}"   # used 10×
  background-contrast-grey-hover:            "{colors.grey-950-100-hover}"   # used 10×
  background-contrast-info:                  "{colors.info-950-100}"   # used 3×
  background-contrast-info-active:           "{colors.info-950-100-active}"   # used 2×
  background-contrast-info-hover:            "{colors.info-950-100-hover}"   # used 2×
  background-contrast-warning:               "{colors.warning-950-100}"   # used 2×
  background-contrast-warning-active:        "{colors.warning-950-100-active}"   # used 2×
  background-contrast-warning-hover:         "{colors.warning-950-100-hover}"   # used 2×
  background-default-grey:                   "{colors.grey-1000-50}"   # used 18×
  background-default-grey-active:            "{colors.grey-1000-50-active}"   # used 15×
  background-default-grey-hover:             "{colors.grey-1000-50-hover}"   # used 15×
  background-disabled-grey:                  "{colors.grey-925-125}"   # used 73×
  background-open-blue-france:               "{colors.blue-france-925-125}"   # used 7×
  background-open-blue-france-active:        "{colors.blue-france-925-125-active}"   # used 5×
  background-open-blue-france-hover:         "{colors.blue-france-925-125-hover}"   # used 5×

  # ---- text ----
  text-action-high-blue-france:              "{colors.blue-france-sun-113-625}"   # used 34×
  text-action-high-grey:                     "{colors.grey-50-1000}"   # used 6×
  text-active-blue-france:                   "{colors.blue-france-sun-113-625}"   # used 8×
  text-default-error:                        "{colors.error-425-625}"   # used 10×
  text-default-grey:                         "{colors.grey-200-850}"   # used 9×
  text-default-info:                         "{colors.info-425-625}"   # used 7×
  text-default-success:                      "{colors.success-425-625}"   # used 9×
  text-disabled-grey:                        "{colors.grey-625-425}"   # used 59×
  text-inverted-blue-france:                 "{colors.blue-france-975-sun-113}"   # used 5×
  text-inverted-grey:                        "{colors.grey-1000-50}"   # used 6×
  text-label-grey:                           "{colors.grey-50-1000}"   # used 8×
  text-mention-grey:                         "{colors.grey-425-625}"   # used 19×
  text-title-grey:                           "{colors.grey-50-1000}"   # used 19×

  # ---- border ----
  border-action-high-blue-france:            "{colors.blue-france-sun-113-625}"   # used 83×
  border-active-blue-france:                 "{colors.blue-france-sun-113-625}"   # used 54×
  border-contrast-grey:                      "{colors.grey-625-425}"   # used 22×
  border-default-beige-gris-galet:           "{colors.beige-gris-galet-main-702}"   # used 14×
  border-default-blue-cumulus:               "{colors.blue-cumulus-main-526}"   # used 14×
  border-default-blue-ecume:                 "{colors.blue-ecume-main-400}"   # used 14×
  border-default-blue-france:                "{colors.blue-france-main-525}"   # used 6×
  border-default-brown-cafe-creme:           "{colors.brown-cafe-creme-main-782}"   # used 14×
  border-default-brown-caramel:              "{colors.brown-caramel-main-648}"   # used 14×
  border-default-brown-opera:                "{colors.brown-opera-main-680}"   # used 14×
  border-default-green-archipel:             "{colors.green-archipel-main-557}"   # used 14×
  border-default-green-bourgeon:             "{colors.green-bourgeon-main-640}"   # used 14×
  border-default-green-emeraude:             "{colors.green-emeraude-main-632}"   # used 14×
  border-default-green-menthe:               "{colors.green-menthe-main-548}"   # used 14×
  border-default-green-tilleul-verveine:     "{colors.green-tilleul-verveine-main-707}"   # used 14×
  border-default-grey:                       "{colors.grey-900-175}"   # used 177×
  border-default-orange-terre-battue:        "{colors.orange-terre-battue-main-645}"   # used 14×
  border-default-pink-macaron:               "{colors.pink-macaron-main-689}"   # used 14×
  border-default-pink-tuile:                 "{colors.pink-tuile-main-556}"   # used 14×
  border-default-purple-glycine:             "{colors.purple-glycine-main-494}"   # used 14×
  border-default-yellow-moutarde:            "{colors.yellow-moutarde-main-679}"   # used 14×
  border-default-yellow-tournesol:           "{colors.yellow-tournesol-main-731}"   # used 14×
  border-disabled-grey:                      "{colors.grey-925-125}"   # used 19×
  border-plain-error:                        "{colors.error-425-625}"   # used 95×
  border-plain-grey:                         "{colors.grey-200-850}"   # used 26×
  border-plain-info:                         "{colors.info-425-625}"   # used 23×
  border-plain-success:                      "{colors.success-425-625}"   # used 93×
  border-plain-warning:                      "{colors.warning-425-625}"   # used 8×
  # ----- END GENERATED DECISION TOKENS -----

  # Literal hex (not a token reference) — DSFR's focus ring is set via the
  # `focus` decision token but compiles to the same hex regardless of theme.
  focus-ring:                      "#0a76f6"

typography:
  # Marianne — sans-serif, the primary government typeface.
  display-xl:
    fontFamily: Marianne
    fontSize: 2.5rem        # 40px
    fontWeight: 700
    lineHeight: 3rem        # 48px
  h1:
    fontFamily: Marianne
    fontSize: 2.5rem
    fontWeight: 700
    lineHeight: 3rem
  h2:
    fontFamily: Marianne
    fontSize: 2rem          # 32px
    fontWeight: 700
    lineHeight: 2.5rem
  h3:
    fontFamily: Marianne
    fontSize: 1.75rem       # 28px
    fontWeight: 700
    lineHeight: 2.25rem
  h4:
    fontFamily: Marianne
    fontSize: 1.5rem        # 24px
    fontWeight: 700
    lineHeight: 2rem
  h5:
    fontFamily: Marianne
    fontSize: 1.25rem       # 20px
    fontWeight: 700
    lineHeight: 1.75rem
  h6:
    fontFamily: Marianne
    fontSize: 1.125rem      # 18px
    fontWeight: 700
    lineHeight: 1.5rem
  body-lg:
    fontFamily: Marianne
    fontSize: 1.125rem      # 18px
    fontWeight: 400
    lineHeight: 1.75rem
  body-md:
    fontFamily: Marianne
    fontSize: 1rem          # 16px
    fontWeight: 400
    lineHeight: 1.5rem
  body-sm:
    fontFamily: Marianne
    fontSize: 0.875rem      # 14px
    fontWeight: 400
    lineHeight: 1.5rem
  body-xs:
    fontFamily: Marianne
    fontSize: 0.75rem       # 12px
    fontWeight: 400
    lineHeight: 1.25rem
  label:
    fontFamily: Marianne
    fontSize: 0.875rem
    fontWeight: 700
    lineHeight: 1.5rem
  # Spectral — serif, secondary; reserved for distinguishing minor/secondary text.
  body-md-alt:
    fontFamily: Spectral
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.5rem
  body-sm-alt:
    fontFamily: Spectral
    fontSize: 0.875rem
    fontWeight: 400
    lineHeight: 1.5rem

rounded:
  none: 0px
  sm:   0.25rem    # used sparingly (search input top corners)
  md:   0.5rem
  pill: 9999px     # tags / badges

spacing:
  # Built on the DSFR `v` base unit: 1v = 0.25rem = 4px.
  # The Figma spec also references "W" units; W = 2v = 8px in this scale.
  0v:    0px
  0-5v:  0.125rem  # 2px
  1v:    0.25rem   # 4px
  1-5v:  0.375rem  # 6px
  2v:    0.5rem    # 8px  (1W)
  3v:    0.75rem   # 12px
  4v:    1rem      # 16px (2W) — standard inter-component gap
  5v:    1.25rem   # 20px
  6v:    1.5rem    # 24px (3W) — typical card padding
  7v:    1.75rem
  8v:    2rem      # 32px (4W) — section spacing
  10v:   2.5rem
  12v:   3rem      # 48px
  16v:   4rem      # 64px
  32v:   8rem      # 128px

components:
  # ============================================================
  # ACTIONS — Buttons (fr-btn, fr-btn--secondary, fr-btn--tertiary)
  # ============================================================
  button-primary:
    backgroundColor: "{colors.text-action-high-blue-france}"
    textColor:       "{colors.text-inverted-grey}"
    typography:      "{typography.body-md}"
    rounded:         "{rounded.none}"
    padding:         16px
    height:          40px
  button-primary-hover:
    backgroundColor: "{colors.background-action-high-blue-france-hover}"
    textColor:       "{colors.text-inverted-grey}"
  button-primary-active:
    backgroundColor: "{colors.background-action-high-blue-france-active}"
    textColor:       "{colors.text-inverted-grey}"
  button-primary-disabled:
    backgroundColor: "{colors.background-contrast-grey}"
    textColor:       "{colors.text-mention-grey}"

  button-secondary:
    backgroundColor: "{colors.background-default-grey}"
    textColor:       "{colors.text-action-high-blue-france}"
    typography:      "{typography.body-md}"
    rounded:         "{rounded.none}"
    padding:         16px
    height:          40px
  button-secondary-hover:
    backgroundColor: "{colors.blue-france-950-100-hover}"
    textColor:       "{colors.text-action-high-blue-france}"
  button-secondary-active:
    backgroundColor: "{colors.blue-france-950-100-active}"
    textColor:       "{colors.text-action-high-blue-france}"

  button-tertiary:
    backgroundColor: "transparent"
    textColor:       "{colors.text-action-high-blue-france}"
    typography:      "{typography.body-md}"
    rounded:         "{rounded.none}"
    padding:         16px
    height:          40px
  button-tertiary-hover:
    backgroundColor: "{colors.background-alt-grey}"
    textColor:       "{colors.text-action-high-blue-france}"

  # ============================================================
  # FORMS — input, select, checkbox, radio, toggle
  # ============================================================
  input:
    backgroundColor: "{colors.background-contrast-grey}"
    textColor:       "{colors.text-default-grey}"
    typography:      "{typography.body-md}"
    rounded:         "{rounded.sm}"
    padding:         12px
    height:          40px
  input-focus:
    backgroundColor: "{colors.background-contrast-grey}"
    textColor:       "{colors.text-default-grey}"
  input-error:
    backgroundColor: "{colors.background-contrast-grey}"
    textColor:       "{colors.text-default-grey}"
  input-disabled:
    backgroundColor: "{colors.background-contrast-grey}"
    textColor:       "{colors.text-mention-grey}"

  select:
    backgroundColor: "{colors.background-contrast-grey}"
    textColor:       "{colors.text-default-grey}"
    typography:      "{typography.body-md}"
    rounded:         "{rounded.sm}"
    padding:         12px
    height:          40px

  checkbox:
    backgroundColor: "{colors.background-default-grey}"
    textColor:       "{colors.text-default-grey}"
    rounded:         "{rounded.none}"
    size:            16px
  checkbox-checked:
    backgroundColor: "{colors.text-action-high-blue-france}"
    textColor:       "{colors.text-inverted-grey}"

  radio:
    backgroundColor: "{colors.background-default-grey}"
    textColor:       "{colors.text-default-grey}"
    rounded:         "{rounded.pill}"
    size:            16px
  radio-checked:
    backgroundColor: "{colors.text-action-high-blue-france}"
    textColor:       "{colors.text-inverted-grey}"

  toggle:
    backgroundColor: "{colors.background-contrast-grey}"
    textColor:       "{colors.text-default-grey}"
    rounded:         "{rounded.pill}"
    width:           40px
    height:          24px
  toggle-on:
    backgroundColor: "{colors.text-action-high-blue-france}"
    textColor:       "{colors.text-inverted-grey}"

  # ============================================================
  # SURFACES — card, tile
  # ============================================================
  card:
    backgroundColor: "{colors.background-default-grey}"
    textColor:       "{colors.text-default-grey}"
    typography:      "{typography.body-md}"
    rounded:         "{rounded.none}"
    padding:         24px
  card-hover:
    backgroundColor: "{colors.background-alt-grey}"
    textColor:       "{colors.text-default-grey}"

  tile:
    backgroundColor: "{colors.background-default-grey}"
    textColor:       "{colors.text-action-high-blue-france}"
    typography:      "{typography.body-md}"
    rounded:         "{rounded.none}"
    padding:         16px
  tile-hover:
    backgroundColor: "{colors.background-alt-grey}"
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

  callout:
    backgroundColor: "{colors.background-alt-grey}"
    textColor:       "{colors.text-default-grey}"
    typography:      "{typography.body-md}"
    rounded:         "{rounded.none}"
    padding:         24px

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

### Scale

| Token | Size | Weight | Use |
|-------|------|--------|-----|
| `display-xl` / `h1` | 2.5rem (40px) | 700 | Hero / page title |
| `h2` | 2rem (32px) | 700 | Major section |
| `h3` | 1.75rem (28px) | 700 | Subsection |
| `h4` | 1.5rem (24px) | 700 | Block heading |
| `h5` | 1.25rem (20px) | 700 | Inline heading |
| `h6` | 1.125rem (18px) | 700 | Smallest heading |
| `body-lg` | 1.125rem (18px) | 400 | Lead paragraph |
| `body-md` | 1rem (16px) | 400 | Default body |
| `body-sm` | 0.875rem (14px) | 400 | Metadata, secondary |
| `body-xs` | 0.75rem (12px) | 400 | Captions, microcopy |
| `label` | 0.875rem (14px) | 700 | Form labels, button text |

Mobile renders one step down on `display-xl`/`h1`/`h2` (handled by `@media` rules in DSFR's CSS — agents emitting markup should rely on the `fr-h1`…`fr-h6` classes which carry the responsive logic).

### Rules

- Body line-height: `1.5rem` (1.5× on `body-md`) for comfortable long-form reading.
- Use sentence case for headings; reserve uppercase for utility microcopy with expanded letter-spacing (e.g. `fr-link--icon` labels).
- **Never** colour a title in Bleu France (see Colors).
- For all-caps utility microcopy, set letter-spacing `0.06em`.

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

The DSFR is built on the **`v` unit**: `1v = 0.25rem = 4px`. The Figma library and the `fr-mb-Xv` / `fr-py-Xv` utility classes both reference this scale.

| Token | Value | Common use |
|-------|-------|------------|
| `1v`  | 4px   | Hairline spacing |
| `2v` (`1W`) | 8px | Tight inline gaps |
| `3v`  | 12px | Compact stack |
| `4v` (`2W`) | 16px | **Default inter-component gap** (button group, form rows) |
| `6v` (`3W`) | 24px | Card / container padding |
| `8v` (`4W`) | 32px | Section spacing |
| `12v` | 48px | Large section gap |
| `16v` | 64px | Hero / page-level rhythm |

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

Corners are **square by convention**. `rounded.none = 0` is the default for almost every component: buttons, cards, modals, alerts, inputs (mostly), tiles, panels.

Documented exceptions:

| Component | Radius | Token |
|-----------|--------|-------|
| Search input (top corners) | 4px | `rounded.sm` |
| Tags, badges, pills | full | `rounded.pill` |
| Toggle switch knob/track | full | `rounded.pill` |

> **Rationale.** Angularity reinforces officiality, restraint, and republican neutrality. Rounded corners would soften the visual register away from the State register the DSFR is designed to preserve.

## Components

Each component below is described once, then surfaced in the YAML token graph as `<component-name>` plus `<component-name>-<state>` entries. State variants follow the alpha `DESIGN.md` convention of separate component entries.

For each component, the **BEM class** column gives the canonical `fr-*` name an implementing agent should emit when generating real HTML — these classes pick up the JS behaviour shipped in `dsfr.module.min.js` automatically.

### Actions

| Component | BEM class | Notes |
|-----------|-----------|-------|
| Primary button | `.fr-btn` | Bleu France background, white text, no radius, 40 px height (`md`). Sizes: `--sm` (32 px), default `md`, `--lg` (48 px). |
| Secondary button | `.fr-btn.fr-btn--secondary` | White background, Bleu France text + 1px border. |
| Tertiary button | `.fr-btn.fr-btn--tertiary` (`--no-outline` for borderless) | Transparent background, Bleu France text. |

Group buttons with `.fr-btns-group` (default vertical with 2W gap; `--inline` for horizontal at a breakpoint; `--equisized` to match widths).

### Forms

| Component | BEM class |
|-----------|-----------|
| Input | `.fr-input` (wrap in `.fr-input-group`; add `.fr-input-group--error` / `--valid` for state) |
| Select | `.fr-select` |
| Checkbox | `.fr-checkbox-group` + native `<input type="checkbox">` |
| Radio | `.fr-radio-group` + native `<input type="radio">` |
| Toggle (interrupteur) | `.fr-toggle` |

Form rules: every input has a visible `<label>`; error messages use `.fr-error-text` with the `error` colour and a 16 px top margin from the input.

### Surfaces

| Component | BEM class |
|-----------|-----------|
| Card (carte) | `.fr-card` (`--horizontal` for side-by-side image; `--no-arrow` to hide the action chevron) |
| Tile (tuile) | `.fr-tile` (smaller, denser variant of card; primary content is a single link) |
| Callout (mise en avant) | `.fr-callout` |

Cards are flat at rest; on `:hover` they may apply `e-3` to suggest interactivity if the entire card is a link.

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
