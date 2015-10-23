from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^view/([0-9]+)/$', views.view, name='view_tercer'),
]

