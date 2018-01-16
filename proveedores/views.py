from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from .forms import ProveedorForm
from .models import Proveedor
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    objetos = Proveedor.objects.all()
    paginator = Paginator(objetos, 1) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        proveedores = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        proveedores = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        proveedores = paginator.page(paginator.num_pages)
    uno = 2 - 1
    return render_to_response('proveedores/index.html', {"proveedores": proveedores})

def nuevoProveedor(request):
    if request.method == "POST":
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proveedores:nuevo')
    else:
        form = ProveedorForm()
    return render(request, 'proveedores/nuevo.html', {'form':form})

def listaProveedores(request, pagina):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedores/'+ pagina + '.html', {'proveedores':proveedores})

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

def eliminarProveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    proveedor.delete()
    return redirect('proveedores:index')
