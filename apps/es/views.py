from django.shortcuts import render, get_object_or_404
from .models import ES


def view(request, ides):
    es = get_object_or_404(ES, pk=int(ides))

    # aixo es una caca pero e sla unica manera de tenir el primer contacte de l'entrada
    if es.factura_interna:
        tercer = es.factura_interna.get_tercer()
        tercer = tercer[tercer.keys()[0]]
    elif es.donacio:
        tercer = es.donacio.tercer

    return render(request, 'es/view.html', { 'es' : es, 'tercer' : tercer })
