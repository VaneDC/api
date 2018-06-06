from django.contrib import admin
from .models import Proveedor

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'mail')
    search_fields = ('nombre','mail')

admin.site.register(Proveedor,ProveedorAdmin)
