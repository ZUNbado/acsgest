from django.contrib import admin
from .models import Periode, Contracte

class ContracteAdmin(admin.ModelAdmin):
    list_display = ( 'expired', 'tercer', 'serveis_to_string', 'alta', 'periode', 'multi', 'comentari')
    list_filter = ( 'expired', 'tercer', 'serveis', 'periode' )


admin.site.register(Periode)
admin.site.register(Contracte, ContracteAdmin)
