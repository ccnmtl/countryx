# flake8: noqa
from countryx.settings_shared import *

try:
    from countryx.local_settings import *
except ImportError:
    pass
