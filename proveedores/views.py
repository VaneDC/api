from django.shortcuts import render
from .forms import ProveedorForm

def index(request):
	return render(request, 'proveedores/index.html')

def nuevoProveedor(request):
    form = ProveedorForm()
    return render(request, 'proveedores/nuevo.html', {'form':form})