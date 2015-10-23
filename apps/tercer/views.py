from django.shortcuts import render, get_object_or_404
from .models import Tercer
from ..contracte.models import Contracte
from ..factura.models import FacturaInterna
from ..es.models import ES


def view(request, tercer_id):
    tercer = get_object_or_404(Tercer, pk=int(tercer_id))
    contractes = Contracte.objects.filter(tercer=tercer)
    factures = FacturaInterna.objects.filter(contracte__in=[c.pk for c in contractes])
    es = ES.objects.filter(factura_interna__in=[f.pk for f in factures])

    info = list()
    for contracte in Contracte.objects.filter(tercer=tercer):
        factures = list()
        for factura in FacturaInterna.objects.filter(contracte=contracte.pk):
            factures.append({
                    'factura' : factura,
                    'es' : ES.objects.filter(factura_interna=factura.pk),
                    })
        info.append({
                'contracte' : contracte,
                'factures' : factures,
                })

    return render(request, 'tercer/view.html', dict(tercer = tercer, info = info ))
