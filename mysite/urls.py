#from django.conf.urls import include, url , 
from django.contrib import admin
from . import views
from django.urls import path, include
from productos.urls import productos_patterns
#from pages.urls import pages_patterns

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    path('', include('core.urls')),
    path('productos/', include(productos_patterns)),
    path('admin/', admin.site.urls),
    #path de la autenticacion
    path('accounts/',include('django.contrib.auth.urls')),
    #url(r'^admin/', admin.site.urls),
    #url(r'^$', views.index, name='index'),
    #url(r'^proveedores/', include('proveedores.urls', namespace="proveedores")),
    #url(r'^productos/', include('productos.urls',namespace="productos")),
    #url(r'^facturaCompra/', include('facturaCompra.urls', namespace="facturaCompra")),
]
