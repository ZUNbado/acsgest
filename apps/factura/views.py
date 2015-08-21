from django.http import HttpResponse
from django.template import RequestContext, loader

from ..contracte.models import Contracte
from .models import FacturaInterna
from ..tercer.models import Tercer, Tipus

from datetime import timedelta, date


# TEST PDF
from django.template.loader import get_template
from django.template import Context
#from django.http import HttpResponse
from cgi import escape
from django.shortcuts import get_object_or_404

def render_to_pdf(template_src, context_dict):
    import cStringIO as StringIO
    import ho.pisa as pisa
    template = get_template(template_src)
    context = Context(context_dict)
    html  = template.render(context)
    result = StringIO.StringIO()

    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), link_callback=fetch_resources, encoding='UTF-8', dest=result,)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))

def fetch_resources(uri, rel):
    path = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ""))
    return path

def genera_factures(request):
    tipus_tercer = Tipus.objects.filter(nom='Soci') | Tipus.objects.filter(nom='Client')

    data = {}
    for tipus in tipus_tercer:
        if tipus.nom not in data: data[tipus.nom] = {}
        for tercer in Tercer.objects.filter(tipus=tipus.pk):
            factura = FacturaInterna()
            factura.quantitat = 0
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

def descarregar_factura(request, idFactura):
    factura = get_object_or_404(FacturaInterna, pk=int(idFactura))
    serveis = {}
    for c in factura.contracte.all():
        for s in c.serveis.all():
            if c.descompte != 0:
                total = ((s.preu * c.multi) - ((s.preu * c.multi * c.descompte) / 100))
            else:
                total = (s.preu * c.multi)
            servei = { 'nom': s.nom, 'preu': s.preu, 'periode': c.periode, 'total': total, 'descompte': c.descompte }
            if s.pk not in serveis: serveis[s.pk]=servei

    return render_to_pdf(
            'factura/pdf.j2',
            {
                'pagesize' : 'A4',
                'serveis' : serveis,
                'factura' : factura,
            }
            )
