from django.contrib import admin
from .models import Tipus, Caixa, Moviment

class CaixaAdmin(admin.ModelAdmin):
    list_display = [ 'nom', 'total' ]

class MovimentAdmin(admin.ModelAdmin):
    list_display = [ 'referencia', 'quantitat', 'caixa_origen', 'caixa_desti', 'data' ]

admin.site.register(Tipus)
admin.site.register(Caixa, CaixaAdmin)
admin.site.register(Moviment, MovimentAdmin)
