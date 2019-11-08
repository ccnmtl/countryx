# flake8: noqa
from countryx.settings_shared import *
from ccnmtlsettings.staging import common
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

locals().update(
    common(
        project=project,
        base=base,
        INSTALLED_APPS=INSTALLED_APPS,
        STATIC_ROOT=STATIC_ROOT,
        cloudfront="dp0pzu8v53cf7",
    ))

try:
    from countryx.local_settings import *
except ImportError:
    pass

if hasattr(settings, 'SENTRY_DSN'):
    sentry_sdk.init(
        dsn=SENTRY_DSN,
        integrations=[DjangoIntegration()],
        debug=True,
    )
