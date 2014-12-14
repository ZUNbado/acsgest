from django.db import models
from ..tercer.models import Tercer
from django.contrib.auth.models import User

class Soci(models.Model):
    nom = models.CharField(max_length=200)
    cognoms = models.CharField(max_length=200)
    dni = models.CharField(max_length=15)
    correu = models.EmailField(max_length=200)
    tercer = models.ForeignKey(Tercer, null=True, blank=True)
    django_user = models.ForeignKey(User, null=True, blank=True)
