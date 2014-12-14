from django.contrib import admin
from .models import Categoria, Servei

class ServeiAdmin(admin.ModelAdmin):
    list_display = ( 'nom', 'categoria', 'preu' )
    list_filter = [ 'categoria' ]
    exclude = ( 'last', 'anterior' )

    def get_queryset(self, request):
        qs = super(ServeiAdmin, self).get_queryset(request)
        return qs.filter(last=True)

admin.site.register(Categoria)
admin.site.register(Servei, ServeiAdmin)

