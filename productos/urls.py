from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^nuevo/$', views.nuevoProducto, name='nuevo'),
    url(r'^editar/(?P<pk>[0-9]+)/edit/$', views.editarProducto, name='editar_producto'),
    url(r'^eliminar/(?P<pk>[0-9]+)/$', views.eliminarProducto, name='eliminar_producto'),
]
