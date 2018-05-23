from django import forms
from .models import facturaCompra
from facturaCompraContieneProductos.models import facturaCompraContieneProductos

class facturaCompraForm(forms.ModelForm):
    
    class Meta:
        model = facturaCompra
        fields = ('idProveedor', 'fecha', 'total')

class facturaCompraContieneProductosForm(forms.ModelForm):
    
    class Meta:
    	model = facturaCompraContieneProductos
    	fields = ('idProducto', 'precio', 'cantidad', 'descuento')