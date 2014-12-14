from django.contrib import admin
from .models import Periode, Contracte

class ContracteAdmin(admin.ModelAdmin):
    list_display = ( 'tercer', 'serveis_to_string', 'alta', 'periode', 'multi', 'comentari')
    list_filter = ( 'tercer', 'serveis', 'periode' )


admin.site.register(Periode)
admin.site.register(Contracte, ContracteAdmin)
