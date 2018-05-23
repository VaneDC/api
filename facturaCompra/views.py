from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import facturaCompra
from facturaCompraContieneProductos.models import facturaCompraContieneProductos
from .forms import facturaCompraForm, facturaCompraContieneProductosForm
from django.views.generic import CreateView

def index(request):
    return render(request, 'facturaCompra/index.html')

'''def nuevaFacturaCompra(request):
    if request.method == 'POST':
        form = facturaCompraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('facturaCompra:nuevo')
    else:
    	form = facturaCompraForm()
    return render(request, 'facturaCompra/nuevo.html', {'form':form})'''

class nuevaFacturaCompra(CreateView):
    model = facturaCompraContieneProductos
    template_name = 'facturaCompra/nuevo.html'
    form_class = facturaCompraContieneProductosForm
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