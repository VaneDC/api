from django.contrib import admin
from .models import facturaCompra , facturaCompraContieneProductos

class facturaCompraAdmin(admin.ModelAdmin):
    list_display = ('idProveedor','total')
    date_hierarchy = 'fecha'
    search_fields = ('idProveedor',)
    list_filter = ('idProveedor',)

class facturaCompraContieneProductosAdmin(admin.ModelAdmin):
    list_display = ('idProducto','precio','cantidad','descuento')

   
admin.site.register(facturaCompra,facturaCompraAdmin)
admin.site.register(facturaCompraContieneProductos,facturaCompraContieneProductosAdmin)

