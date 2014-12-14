from django.db import models
from datetime import datetime
#from ..es.models import ES

class Tipus(models.Model):
    nom = models.CharField(max_length=200)

    def __unicode__(self):
        return u'%s' % self.nom

    class Meta:
        verbose_name_plural = u'Tipus'

class Caixa(models.Model):
    nom = models.CharField(max_length=200)
    tipus = models.ForeignKey(Tipus)
    comentari = models.CharField(max_length=200)
    total = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)

    def __unicode__(self):
        return u'%s' % self.nom

    class Meta:
        verbose_name_plural = u'Caixes'

class Moviment(models.Model):
    referencia = models.CharField(max_length=200)
    quantitat = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    caixa_origen = models.ForeignKey(Caixa, related_name='caixaorigen')
    caixa_desti = models.ForeignKey(Caixa, related_name='caixadesti')
    data = models.DateField(default=datetime.now) 

    def __unicode__(self):
        return u'%s' % self.referencia

    def save(self, *args, **kwargs):
        super(Moviment, self).save(*args, **kwargs)
        self.crea_es()

    def crea_es(self):
        from ..es.models import ES
        (entrada, nova) = ES.objects.get_or_create(moviment=self, caixa=self.caixa_desti)
        entrada.quantitat = self.quantitat
        entrada.data = self.data
        entrada.referencia = self.referencia
        entrada.moviment = self
        entrada.save()

        (sortida, nova) = ES.objects.get_or_create(moviment=self, caixa=self.caixa_origen)
        sortida.entrada = False
        sortida.quantitat = self.quantitat
        sortida.data = self.data
        sortida.referencia = self.referencia
        sortida.moviment = self
        sortida.save()
