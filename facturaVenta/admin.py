from django.contrib import admin
from django.contrib import admin
from .models import facturaVenta , facturaVentaContieneProductos

class facturaVentaAdmin(admin.ModelAdmin):
    list_display = ('idMedioDePago', 'idTipoDeVenta', 'total')
    date_hierarchy = 'fecha'
    list_filter = ('idTipoDeVenta',)

class facturaVentaContieneProductosAdmin(admin.ModelAdmin):
    list_display = ('idProducto','precio','cantidad','descuento')


admin.site.register(facturaVenta,facturaVentaAdmin)
admin.site.register(facturaVentaContieneProductos,facturaVentaContieneProductosAdmin)