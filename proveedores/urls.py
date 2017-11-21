from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^nuevo/$', views.nuevoProveedor, name='nuevo'),
    url(r'^lista/$', views.listaProveedores, name="lista"),
    url(r'^editar/(?P<pk>[0-9]+)/edit/$', views.editarProveedor, name='editar_proveedor'),
]