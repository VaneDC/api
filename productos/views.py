from django.shortcuts import render, redirect
from .forms import ProductoForm
# Create your views here.


def index(request):
    return render(request, 'productos/index.html')

def nuevoProducto(request):
    form = ProductoForm()
    return render(request, 'productos/nuevo.html', {'form':form})

    
#def nuevoProducto(request):
#    if request.method == 'POST':
#        form = ProductoForm(request.POST)
#        if form.is_valid():
#       	    form.save()
#            return render(request, 'productos/nuevo.html', {'form':form})
#        else:
#            form = ProductoForm()
#    return render(request, 'productos/nuevo.html', {'form':form})