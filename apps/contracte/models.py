from django.db import models
from ..tercer.models import Tercer
from ..servei.models import Servei


class Periode(models.Model):
    nom = models.CharField(max_length=20)
    periode = models.IntegerField(default=30)

    def __unicode__(self):
        return u'%s' % self.nom

class Contracte(models.Model):
    tercer = models.ForeignKey(Tercer)
    serveis = models.ManyToManyField(Servei)
    periode = models.ForeignKey(Periode)
    comentari = models.CharField(max_length=200,null=True,blank=True)
    multi = models.IntegerField(default=1)
    descompte = models.DecimalField(max_digits=5, default=0, decimal_places=2,null=True,blank=True)
    alta = models.DateField(null=True,blank=True)
    actiu = models.BooleanField(default=True)

    def serveis_to_string(self):
        srv = []
        for s in self.serveis.all():
            srv.append(s.nom)
        return ','.join(srv)

    def __unicode__(self):
        return u'%d / %s / %s' % (self.id, self.tercer, self.serveis_to_string())
