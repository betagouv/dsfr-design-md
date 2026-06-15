#!/usr/bin/env python3
"""Single source of truth for the DSFR reference version.

Any script that fetches DSFR assets (CSS, fonts, etc.) must import from
this module instead of hardcoding a version string.
"""

DSFR_VERSION = "1.14.4"
DSFR_CSS_URL = f"https://cdn.jsdelivr.net/npm/@gouvfr/dsfr@{DSFR_VERSION}/dist/dsfr.css"

