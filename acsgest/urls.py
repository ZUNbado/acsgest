from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


from rest_framework.routers import DefaultRouter
router = DefaultRouter()

api_models = [
        ( 'apps.tercer.viewsets', 'TercerViewSet', 'tercer' ),
        ( 'apps.caixa.viewsets', 'CaixaViewSet', 'caixa' ),
        ]
for (module, model, route) in api_models:
    router.register(route, getattr(__import__(module, fromlist=[model]), model)) 

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url='/admin')),
    url(r'^api/', include(router.urls)),
#    url(r'^$', include('apps.public.urls')),
    url(r'^public/', include('apps.public.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^factura/', include('apps.factura.urls')),
) + staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
