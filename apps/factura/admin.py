from django.contrib import admin
from .models import FacturaInterna, FacturaExterna
from ..es.models import ES

class ESInline(admin.StackedInline):
    model = ES
    extra = 0
    fields = ( 'entrada', 'referencia', 'quantitat', 'caixa', 'data' )


class FacturaInternaAdmin(admin.ModelAdmin):
    inlines = [ ESInline, ]
    list_display = [ 'id', 'creacio', 'quantitat', 'pagat', 'estat', 'pagament', 'tercer', 'serveis' ]
    list_filter = [ 'estat', 'contracte' ]
    ordering = [ '-creacio' ]
    fieldsets = (
        (None, {
            'fields': ( 'referencia', 'contracte', 'estat', 'creacio', 'pagament', 'quantitat', 'descompte', 'pagat', 'comentari' )
        }),
    )

class FacturaExternaAdmin(admin.ModelAdmin):
    inlines = [ ESInline, ]
    list_display = [ 'id', 'tercer', 'referencia', 'creacio', 'quantitat', 'pagat', 'estat', 'pagament' ]
    list_filter = [ 'estat', 'tercer' ]
    ordering = [ '-creacio' ]


admin.site.register(FacturaInterna, FacturaInternaAdmin)
admin.site.register(FacturaExterna, FacturaExternaAdmin)
