#from django.shortcuts import render, get_object_or_404, redirect, render_to_response
#from .forms import ProductoForm
#from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#from django.http import HttpResponse
#import json
# Create your views here.
from .models import Producto
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

#para mostrar la lista de productos
class ProductoListView(ListView):
    model = Producto

#Para ver un producto en particular
class ProductoDetailView(DetailView):
    model = Producto

#Para crear un producto
class ProductoCreate(CreateView):
    model = Producto
    fields = ['nombre','descripcion','stock','stock_minimo','costo','precio_minorista','precio_mayorista']
    success_url = reverse_lazy('productos:productos')

#Para editar un producto
class ProductoUpdate(UpdateView):
    model = Producto
    fields = ['nombre','descripcion','stock','stock_minimo','costo','precio_minorista','precio_mayorista']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('productos:editar',args=[self.object.idProducto]) + '?ok'

#Para borrar un producto
class ProductoDelete(DeleteView):
    model = Producto
    success_url = reverse_lazy('productos:productos')


#def index(request):
#    objetos = Producto.objects.all()
#    paginator = Paginator(objetos, 1) # Show 25 contacts per page
#    page = request.GET.get('page')
#    try:
#        productos = paginator.page(page)
#    except PageNotAnInteger:
#        # If page is not an integer, deliver first page.
#        productos = paginator.page(1)
#    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.#
 #       productos = paginator.page(paginator.num_pages)
#    uno = 2 - 1
#    return render_to_response('productos/index.html', {"productos": productos})

    
#def nuevoProducto(request):
#    if request.method == 'POST':
#        form = ProductoForm(request.POST)
##        if form.is_valid():
#       	    form.save()
#            return redirect('productos:nuevo')
#    else:
#        form = ProductoForm()
#    return render(request, 'productos/nuevo.html', {'form':form})

#def listaProductos(request, pagina):
#    productos = Producto.objects.all()
#    return render(request, 'productos/'+ pagina + '.html', {'productos':productos})

#def editarProducto(request, pk):
#    producto = get_object_or_404(Producto, pk=pk)
##    if request.method == "POST":
##        form = ProductoForm(request.POST, instance=producto)
#        if form.is_valid():
#            producto = form.save()
#            return redirect('/productos/')
#    else:
 #       form = ProductoForm(instance=producto)
 #   return render(request, 'productos/editar.html', {'form': form})

#def eliminarProducto(request, pk):
#    producto = get_object_or_404(Producto, pk=pk)
#    producto.delete()
#    return redirect('productos:index')

#def buscarProducto(request):
#    if request.is_ajax():
#        search=request.GET.get('start','')
#        productos = Producto.objects.filter(nombre__icontains=search)
#        results=[]
#        for producto in productos:
#            producto_json={}
#            producto_json['label']=producto.nombre
#            producto_json['value']=producto.nombre
##            results.append(producto_json)
#        data_json=json.dumps(results)
#        return HttpResponse(data_json, content_type='application/json')
#    else:
#        return redirect("productos:index")    