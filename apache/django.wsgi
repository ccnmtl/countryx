import os, sys, site

# enable the virtualenv
site.addsitedir('/var/www/countryx/countryx/ve/lib/python2.6/site-packages')

# paths we might need to pick up the project's settings
sys.path.append('/var/www/countryx/countryx/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'countryx.settings_production'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
