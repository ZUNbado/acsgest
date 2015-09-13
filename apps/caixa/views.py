from django.http import HttpResponse
from django.template import RequestContext, loader
from ..es.models import ES

def resume(request):
    all_es = ES.objects.all()

    data = {}
    for es in all_es:
        if es.data.year not in data: data[es.data.year] = { 'total' : 0, 'months' : {} }
        if es.data.month not in data[es.data.year]['months']: 
            data[es.data.year]['months'][es.data.month] = { 'total' : 0, 'es' : {} }
            data[es.data.year]['months'][es.data.month]['es'] = { 
                    'factura_interna' : { 'total' : 0, 'es' : [] }, 
                    'factura_externa' : { 'total' : 0, 'es' : [] }, 
                    'donacio' : { 'total' : 0, 'es' : [] },
                    'other' : { 'total' : 0, 'es' : [] },
                    } 

        dest = 'other'
        for tipus in [ 'factura_interna', 'factura_externa', 'donacio' ]:
            if getattr(es, tipus):
                dest = tipus

        data[es.data.year]['months'][es.data.month]['es'][dest]['es'].append(es)
        if es.entrada:
            data[es.data.year]['months'][es.data.month]['es'][dest]['total'] += es.quantitat
            data[es.data.year]['months'][es.data.month]['total'] += es.quantitat
            data[es.data.year]['total'] += es.quantitat
        else:
            data[es.data.year]['months'][es.data.month]['es'][dest]['total'] -= es.quantitat
            data[es.data.year]['months'][es.data.month]['total'] -= es.quantitat
            data[es.data.year]['total'] -= es.quantitat

    template = loader.get_template('es/resume.html.j2')
    context = RequestContext(request, {
        'data': data,
        })
    return HttpResponse(template.render(context))
