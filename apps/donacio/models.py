from django.db import models
from datetime import datetime
from ..tercer.models import Tercer

class Donacio(models.Model):
    tercer = models.ForeignKey(Tercer,null=True,blank=True)
    quantitat = models.IntegerField()
    data = models.DateField(default=datetime.now)
    comentari = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = u'Donacions'
