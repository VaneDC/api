from django import forms
from .models import facturaCompra

class facturaCompraForm(forms.ModelForm):
    
    class Meta:
        model = facturaCompra
        fields = ('idProveedor', 'fecha', 'total')