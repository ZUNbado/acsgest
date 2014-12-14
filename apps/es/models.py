from django.db import models
from datetime import datetime
from django.db.models.signals import post_delete
from django.dispatch.dispatcher import receiver
from ..caixa.models import Caixa, Moviment
from ..factura.models import FacturaInterna, FacturaExterna
from ..donacio.models import Donacio


class ES(models.Model):
    entrada = models.BooleanField(default=True)
    quantitat = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    caixa = models.ForeignKey(Caixa)
    referencia = models.CharField(max_length=200,null=True,blank=True)
    factura_interna = models.ForeignKey(FacturaInterna,null=True,blank=True)
    factura_externa = models.ForeignKey(FacturaExterna,null=True,blank=True)
    donacio = models.ForeignKey(Donacio,null=True,blank=True)
    moviment = models.ForeignKey(Moviment,null=True,blank=True)
    data = models.DateField(default=datetime.now)
    comentari = models.CharField(max_length=200,null=True,blank=True)

    def save(self, *args, **kwargs):
        super(ES, self).save(*args, **kwargs)
        self.actualitza_caixa()
        self.actualitza_factures()

    def actualitza_factures(self):
        if self.factura_externa is not None:
            quantitat = 0
            for e in ES.objects.filter(factura_externa=self.factura_externa):
                quantitat = quantitat + e.quantitat
            self.factura_externa.pagat = quantitat
            self.factura_externa.pagament = self.data
            self.factura_externa.save()

        if self.factura_interna is not None:
            quantitat = 0
            for e in ES.objects.filter(factura_interna=self.factura_interna):
                quantitat = quantitat + e.quantitat
            self.factura_interna.pagat = quantitat
            self.factura_interna.pagament = self.data
            self.factura_interna.save()

    def actualitza_caixa(self):
        total = 0
        for es in ES.objects.filter(caixa=self.caixa):
            if es.entrada == True:
                if es.quantitat is not None:
                    total = total + es.quantitat
            else:
                if es.quantitat is not None:
                    total = total - es.quantitat
        self.caixa.total = total
        self.caixa.save()

    class Meta:
        verbose_name = u'Entrada/Sortida'
        verbose_name_plural = u'Entrades/Sortides'


@receiver(post_delete, sender=ES)
def delete_es(sender, instance, **kwargs):
        instance.actualitza_caixa()
        instance.actualitza_factures()
