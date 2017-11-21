from django.shortcuts import render, get_object_or_404
from .forms import ProveedorForm
from django.shortcuts import redirect
from .models import Proveedor

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

def listaProveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedores/lista.html', {'proveedores':proveedores})

def editarProveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == "POST":
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            proveedor = form.save()
            return redirect('/proveedores/lista')
    else:
        form = ProveedorForm(instance=proveedor)
    return render(request, 'proveedores/editar.html', {'form': form})