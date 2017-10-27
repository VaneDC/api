from django.shortcuts import render
from .forms import ProveedorForm
from django.shortcuts import redirect

def index(request):
	return render(request, 'proveedores/index.html')

def nuevoProveedor(request):
    if request.method == "POST":
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proveedores:nuevo')
    else:
        form = ProveedorForm()
    return render(request, 'proveedores/nuevo.html', {'form':form})