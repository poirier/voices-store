from warnings import warn
from django.conf import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^staff/', include('staff.urls', app_name='staff')),
    url(r'^users/', include('users.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^', include('store.urls')),
)


# make sure required settings are set
required = ['STRIPE_SECRET_KEY', 'STRIPE_PUBLISHABLE_KEY', 'MEMBER_PASSWORD',
            'CONTACT_EMAILS', 'SITE_ID']
for name in required:
    if not hasattr(settings, name):
        warn("Required setting '%s' is missing. Required settings are %r" % (name, required))
