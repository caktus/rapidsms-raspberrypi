from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from rapidsms.backends.kannel.views import KannelBackendView


admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    # RapidSMS core URLs
    (r'^accounts/', include('rapidsms.urls.login_logout')),
    url(r'^$', 'rapidsms.views.dashboard', name='rapidsms-dashboard'),
    # RapidSMS contrib app URLs
    (r'^export/', include('rapidsms.contrib.export.urls')),
    url(r'^httptester/$',
        'rapidsms.contrib.httptester.views.generate_identity',
        {'backend_name': 'message_tester'}, name='httptester-index'),
    (r'^httptester/', include('rapidsms.contrib.httptester.urls')),
    (r'^locations/', include('rapidsms.contrib.locations.urls')),
    (r'^messagelog/', include('rapidsms.contrib.messagelog.urls')),
    (r'^messaging/', include('rapidsms.contrib.messaging.urls')),
    (r'^registration/', include('rapidsms.contrib.registration.urls')),
    # backends
    url(r"^backend/kannel-usb0-smsc/$",
        KannelBackendView.as_view(backend_name="kannel-usb0-smsc")),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
