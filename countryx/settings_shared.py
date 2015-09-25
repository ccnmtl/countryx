# Django settings for countryx project.
import os.path
from ccnmtlsettings.shared import common

project = 'countryx'
base = os.path.dirname(__file__)

locals().update(
    common(
        project=project,
        base=base,
    ))

PROJECT_APPS = ['countryx.sim', ]

MIDDLEWARE_CLASSES += [  # noqa
    'countryx.sim.middleware.GameStateMiddleware',
]

INSTALLED_APPS += [  # noqa
    'countryx.sim',
]
