from django.contrib import admin
from .models import facturaCompra , facturaCompraContieneProductos

admin.site.register(facturaCompra)
admin.site.register(facturaCompraContieneProductos)

