from django.forms.models import inlineformset_factory
from django import forms
from .models import facturaCompra , facturaCompraContieneProductos


class facturaCompraForm(forms.ModelForm):
    
    class Meta:
        model = facturaCompra
        fields = ('idProveedor', 'fecha', 'total')

class facturaCompraContieneProductosForm(forms.ModelForm):
    
    class Meta:
    	model = facturaCompraContieneProductos
    	fields = ('idProducto', 'precio', 'cantidad', 'descuento')

facturaCompraContieneProductosFormSet = inlineformset_factory(facturaCompra, facturaCompraContieneProductos, form=facturaCompraContieneProductosForm, extra=2)