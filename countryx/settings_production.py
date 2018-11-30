# flake8: noqa
from countryx.settings_shared import *
from ccnmtlsettings.production import common

locals().update(
    common(
        project=project,
        base=base,
        INSTALLED_APPS=INSTALLED_APPS,
        STATIC_ROOT=STATIC_ROOT,
        cloudfront="d3pm8n47h5kmes",
    ))

try:
    from countryx.local_settings import *
except ImportError:
    pass
