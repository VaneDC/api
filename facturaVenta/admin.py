from django.contrib import admin
from django.contrib import admin
from .models import facturaVenta , facturaVentaContieneProductos

admin.site.register(facturaVenta)
admin.site.register(facturaVentaContieneProductos)