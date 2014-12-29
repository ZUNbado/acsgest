from django.contrib import admin
from .models import Donacio
from ..es.models import ES

class ESInline(admin.StackedInline):
    model = ES
    extra = 0
    fields = ( 'entrada', 'referencia', 'quantitat', 'caixa', 'data' )

class DonacioAdmin(admin.ModelAdmin):
    inlines = [ ESInline, ]
    list_display = [ 'tercer', 'quantitat', 'data', 'comentari' ]

admin.site.register(Donacio, DonacioAdmin)
