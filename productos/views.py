from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from .forms import ProductoForm
from .models import Producto
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
import json
# Create your views here.

def index(request):
    objetos = Producto.objects.all()
    paginator = Paginator(objetos, 1) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        productos = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        productos = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        productos = paginator.page(paginator.num_pages)
    uno = 2 - 1
    return render_to_response('productos/index.html', {"productos": productos})

    
def nuevoProducto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
       	    form.save()
            return redirect('productos:nuevo')
    else:
        form = ProductoForm()
    return render(request, 'productos/nuevo.html', {'form':form})

def listaProductos(request, pagina):
    productos = Producto.objects.all()
    return render(request, 'productos/'+ pagina + '.html', {'productos':productos})

def editarProducto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            producto = form.save()
            return redirect('/productos/')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'productos/editar.html', {'form': form})

def eliminarProducto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    producto.delete()
    return redirect('productos:index')

def buscarProducto(request):
    if request.is_ajax():
        search=request.GET.get('start','')
        productos = Producto.objects.filter(nombre__icontains=search)
        results=[]
        for producto in productos:
            producto_json={}
            producto_json['label']=producto.nombre
            producto_json['value']=producto.nombre
            results.append(producto_json)
        data_json=json.dumps(results)
        return HttpResponse(data_json, content_type='application/json')
    else:
        return redirect("productos:index")    