from django.conf.urls.static import static
from django.conf.urls import patterns, url, include
from pastebin.settings import local as settings

from django.contrib import admin

from pastebin.apps.views import index, detail

admin.autodiscover()

urlpatterns = patterns('',
   # (r'', include('pastebin.apps.')),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    url(r'^detail/(?P<id>[A-Za-z0-9]+)/', detail, name='detail'),
    (r'', index)
)

if settings.DEBUG and settings.MEDIA_ROOT:
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)