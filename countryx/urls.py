from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView


admin.autodiscover()

urlpatterns = [
    url(r'^$', 'countryx.sim.views.root'),
    url('^accounts/', include('djangowind.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^impersonate/', include('impersonate.urls')),
    url(r'^sim/', include('countryx.sim.urls')),
    url(r'^smoketest/', include('smoketest.urls')),
    url('^stats/', TemplateView.as_view(template_name='stats.html')),
    url(r'^uploads/(?P<path>.*)$',
        'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^about', TemplateView.as_view(template_name='flatpages/about.html')),
    url(r'^help', TemplateView.as_view(template_name='flatpages/help.html')),
    url(r'^contact',
        TemplateView.as_view(template_name='flatpages/contact.html')),
]
