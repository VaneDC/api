from django.shortcuts import render, redirect
from .models import facturaCompra
from .forms import facturaCompraForm

def index(request):
    return render(request, 'facturaCompra/index.html')

def nuevaFacturaCompra(request):
    if request.method == 'POST':
        form = facturaCompraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('facturaCompra:nuevo')
    else:
    	form = facturaCompraForm()
    return render(request, 'facturaCompra/nuevo.html', {'form':form})