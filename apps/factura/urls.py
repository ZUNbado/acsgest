from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^genera_factures$', views.genera_factures, name='genera_factures'),
]

