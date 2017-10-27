from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        
        fields = ('nombre', 'descripcion', 'stock', 'stock_minimo','costo','precio_minorista','precio_mayorista')
        

        #labels = {
        #    'nombre': 'Nombre', 
        #    'descripcion' : 'Descripcion', 
        #    'stock' : 'Stock', 
        #    'stock_minimo' : 'Stock Minimo',
        #    'costo' : 'Costo',
        #    'precio_minorista' : 'Precio Minorista',
        #    'precio_mayorista' : 'Precio Mayorista',
        #}

        #widgets = {
        #    'nombre': forms.TextImput(attrs={'class':'form-control'}), 
        #    'descripcion' : forms.TextImput(attrs={'class':'form-control'}), 
        #    'stock' : forms.TextImput(attrs={'class':'form-control'}), 
        #    'stock_minimo' : forms.TextImput(attrs={'class':'form-control'}),
        #    'costo' : forms.TextImput(attrs={'class':'form-control'}),
        #    'precio_minorista' : forms.TextImput(attrs={'class':'form-control'}),
        #    'precio_mayorista' : forms.TextImput(attrs={'class':'form-control'}),
        #}