from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^resume$', views.resume, name='es_resume'),
]

