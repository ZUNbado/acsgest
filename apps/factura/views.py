from django.http import HttpResponse
from django.template import RequestContext, loader

from ..contracte.models import Contracte
from .models import FacturaInterna
from ..tercer.models import Tercer, Tipus

from datetime import timedelta, date


def genera_factures(request):
    tipus_tercer = Tipus.objects.filter(nom='Soci') | Tipus.objects.filter(nom='Client')

    data = {}
    for tipus in tipus_tercer:
        if tipus.nom not in data: data[tipus.nom] = {}
        for tercer in Tercer.objects.filter(tipus=tipus.pk):
            factura = FacturaInterna()
            if tercer.nom not in data[tipus.nom]: data[tipus.nom][tercer.nom] = []
            for c in Contracte.objects.filter(actiu=True,tercer=tercer.pk):
                duracio = timedelta(days=c.periode.periode)
                afegir_contracte = True
                if c.alta is None:
                    factura.cracio = date.today
                else:
                    factura.creacio = c.alta

                for f in FacturaInterna.objects.filter(contracte=c):
                    if f.creacio is not None and date.today() <= f.creacio + duracio :
                        afegir_contracte = False

                    if f.creacio is not None and f.creacio + duracio > factura.creacio:
                        factura.creacio = f.creacio + duracio

                if afegir_contracte == True:
                    if c not in data[tipus.nom][tercer.nom]: data[tipus.nom][tercer.nom].append(c)
                    factura.save()
                    factura.contracte.add(c.pk)
                    factura.save()

    template = loader.get_template('factura/genera_factures.html.j2')
    context = RequestContext(request, {
        'data': data,
    })

    return HttpResponse(template.render(context))

