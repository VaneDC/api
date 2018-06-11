from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'stock', 'stock_minimo','costo','precio_minorista','precio_mayorista']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'nombre'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control', 'placeholder':'descripcion'}),
            'stock': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'  '}),
            'stock_minimo': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'  '}),
            'costo': forms.NumberInput(attrs={'class':'form-control', 'placeholder':' '}),
            'precio_minorista': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'  '}),
            'precio_mayorista': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'  '}),
        }
    
     