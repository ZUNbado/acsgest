from django.db import models

class Tipus(models.Model):
    nom = models.CharField(max_length=80)

    def __unicode__(self):
        return u'%s' % self.nom

    class Meta:
        verbose_name_plural = u'Tipus'

class Tercer(models.Model):
    nom = models.CharField(max_length=80)
    cognom1 = models.CharField(max_length=80)
    cognom2 = models.CharField(max_length=80)
    dni = models.CharField(max_length=80)
    correu = models.CharField(max_length=80)
    tipus = models.ForeignKey(Tipus)
    actiu = models.BooleanField(default=0)
    colectiu = models.BooleanField(default=0)

    def __unicode__(self):
        return u'%s' % self.nom
