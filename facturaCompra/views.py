from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import facturaCompra , facturaCompraContieneProductos
from .forms import facturaCompraForm, facturaCompraContieneProductosFormSet
from django.views.generic import CreateView

def index(request):
    return render(request, 'facturaCompra/index.html')

class nuevaFacturaCompra(CreateView):
    model = facturaCompra
    template_name = 'facturaCompra/nuevo.html'
    form_class = facturaCompraForm
    success_url = reverse_lazy('facturaCompra:index')

    def get(self, request, *args, **kwargs):
       self.object = None
       form_class = self.get_form_class()
       form = self.get_form(form_class) 
       productosCompraFormSet = facturaCompraContieneProductosFormSet()
       return self.render_to_response(self.get_context_data(form=form, productosCompraFormSet=productosCompraFormSet))
    
    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        productosCompraFormSet = facturaCompraContieneProductosFormSet(request.POST)
        if form.is_valid() and productosCompraFormSet.is_valid():
            return self.form_valid(form, productosCompraFormSet)
        else:
            return self.form_invalid(form, productosCompraFormSet)

    def form_valid(self, form, productosCompraFormSet):
        self.object = form.save()
        productosCompraFormSet.instance = self.object
        productosCompraFormSet.save()
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form, productosCompraFormSet):
        return self.render_to_response(self.get_context_data(form=form, productosCompraFormSet=productosCompraFormSet))


'''class nuevaFacturaCompra(CreateView):
    
    model = facturaCompraContieneProductos
    template_name = 'facturaCompra/nuevo.html'
    form_class = facturaCompraContieneProductosFormSet
    second_form_class = facturaCompraForm
    success_url = reverse_lazy('facturaCompra:index')

    def get_context_data(self, **kwargs):
        context = super(nuevaFacturaCompra, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            facturaContiene = form.save(commit=False)
            facturaContiene.idFacturaCompra = form2.save()
            facturaContiene.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))
'''

