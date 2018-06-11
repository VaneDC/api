from django.conf.urls import include, url
from django.urls import path
from .views import ProductoListView, ProductoDetailView, ProductoCreate, ProductoUpdate, ProductoDelete

#app_name = 'productos'
productos_patterns = ([
   path('',ProductoListView.as_view(), name='productos'),
   path('<int:pk>/<slug:slug>/',ProductoDetailView.as_view(), name ='producto'),
   path('crear/', ProductoCreate.as_view(), name='crear'),
   path('editar/<int:pk>/', ProductoUpdate.as_view(), name='editar'),
   path('borrar/<int:pk>/', ProductoDelete.as_view(), name='borrar'),
   # url(r'^$', views.index, name='index'),
   # url(r'^nuevo/$', views.nuevoProducto, name='nuevo'),
   # url(r'^editar/(?P<pk>[0-9]+)/edit/$', views.editarProducto, name='editar_producto'),
   # url(r'^eliminar/(?P<pk>[0-9]+)/$', views.eliminarProducto, name='eliminar_producto'),
   # url(r'^busqueda/$', views.buscarProducto, name="buscar_producto"),
],'productos')
