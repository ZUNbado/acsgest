from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^genera_factures$', views.genera_factures, name='genera_factures'),
    url(r'^descarrega_factura/([0-9]+)/$', views.descarregar_factura, name='descarregar_factura'),
]

