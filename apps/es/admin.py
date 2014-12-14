from django.contrib import admin
from .models import ES

class ESAdmin(admin.ModelAdmin):
    list_display = [ 'entrada', 'quantitat', 'caixa', 'referencia', 'data' ]
    list_filter = [ 'entrada', 'caixa' ]
    ordering = [ '-data' ]

admin.site.register(ES, ESAdmin)
