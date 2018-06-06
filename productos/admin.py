from django.contrib import admin
from .models import Producto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'stock', 'costo','precio_minorista','precio_mayorista')
    search_fields = ('nombre','descripcion')
    list_filter = ('precio_minorista','precio_mayorista')
    
admin.site.register(Producto,ProductoAdmin)