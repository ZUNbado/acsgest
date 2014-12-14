from django.db import models
from django.db.models.signals import post_delete
from django.dispatch.dispatcher import receiver


class Categoria(models.Model):
    nom = models.CharField(max_length=80)

    def __unicode__(self):
        return u'%s' % self.nom

class Servei(models.Model):
    nom = models.CharField(max_length=80)
    categoria = models.ForeignKey(Categoria)
    preu = models.DecimalField(max_digits=5, decimal_places=2)
    anterior = models.ForeignKey('self',null=True,blank=True)
    last = models.BooleanField(default=True)
    
    def __unicode__(self):
        return u'%s' % self.nom

    def save(self, *args, **kwargs):
        if self.pk:
            ant = Servei.objects.get(pk=self.pk)
            if ant.nom != self.nom or ant.preu != self.preu or ant.categoria != self.categoria:
                self.anterior=self
                self.pk=None
                ant.last=False
                ant.save()
        super(Servei, self).save(*args, **kwargs)

@receiver(post_delete, sender=Servei)
def set_last_servei(sender, instance, **kwargs):
    ant=instance.anterior
    if ant is not None:
        ant.last=True
        ant.save()
