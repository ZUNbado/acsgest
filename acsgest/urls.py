from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'acsgest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', RedirectView.as_view(url='/admin')),
#    url(r'^$', include('apps.public.urls')),
    url(r'^public/', include('apps.public.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^factura/', include('apps.factura.urls')),
) + staticfiles_urlpatterns()
