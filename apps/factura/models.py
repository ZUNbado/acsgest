from django.db import models
from datetime import datetime, date
from ..contracte.models import Contracte
from ..tercer.models import Tercer


class FacturaInterna(models.Model):
    referencia = models.CharField(max_length=200,null=True,blank=True)
    creacio = models.DateField(default=datetime.now)
    pagament = models.DateField(null=True,blank=True)
    estat = models.BooleanField(default=False)
    contracte = models.ManyToManyField(Contracte)
    quantitat = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    descompte = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    pagat = models.DecimalField(max_digits=5, decimal_places=2,null=True,blank=True)
    comentari = models.CharField(max_length=200,null=True,blank=True)

    def __unicode__(self):
        return u'%d' % self.id

    def save(self, *args, **kwargs):
        self.total()
        self.actualitza_estat()
        super(FacturaInterna, self).save(*args, **kwargs)

    def actualitza_estat(self):
        if self.pagat == self.quantitat + self.descompte:
            self.estat = True
        else:
            self.estat = False

    def tercer(self):
        tercers = []
        for c in self.contracte.all():
            if c.tercer.nom not in tercers:
                tercers.append(c.tercer.nom)
        return u','.join(tercers)
    def serveis(self):
        serveis = []
        for c in self.contracte.all():
            for s in c.serveis.all():
                serveis.append(s.nom)
        return u','.join(serveis)

    def total(self):
        quantitat = 0
        if self.id:
            for c in self.contracte.all():
                for s in c.serveis.all():
                    if c.descompte != 0:
                        quantitat = quantitat + ((s.preu * c.multi) - ((s.preu * c.multi * c.descompte) / 100))
                    else:
                        quantitat = quantitat +  (s.preu * c.multi)
            self.quantitat = quantitat

    class Meta:
        verbose_name_plural = u'Factures Internes'


class FacturaExterna(models.Model):
    referencia = models.CharField(max_length=200)
    tercer = models.ForeignKey(Tercer, null=True, blank=True)
    creacio = models.DateField(default=datetime.now)
    pagament = models.DateField(null=True,blank=True)
    estat = models.BooleanField(default=False)
    quantitat = models.DecimalField(max_digits=5, decimal_places=2,null=True,blank=True)
    pagat = models.DecimalField(max_digits=5, decimal_places=2,null=True,blank=True)
    comentari = models.CharField(max_length=200,null=True,blank=True)

    def __unicode__(self):
        return u'%s / %s' % (self.tercer, self.referencia)


    def actualitza_estat(self):
        if self.pagat == self.quantitat:
            self.estat = True
        else:
            self.estat = False

    def save(self, *args, **kwargs):
        self.actualitza_estat()
        super(FacturaExterna, self).save(*args, **kwargs)


    class Meta:
        verbose_name_plural = u'Facutres Externes'
