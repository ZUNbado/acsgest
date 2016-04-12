from django.contrib import admin
from .models import Tercer, Tipus

class TercerAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'nom', 'cognom1', 'cognom2', 'correu', 'tipus', 'actiu', 'colectiu' ]
    list_filter = [ 'tipus' ]

admin.site.register(Tercer, TercerAdmin)
admin.site.register(Tipus)
