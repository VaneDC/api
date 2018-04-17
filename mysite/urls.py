from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^proveedores/', include('proveedores.urls', namespace="proveedores")),
    url(r'^productos/', include('productos.urls',namespace="productos")),
]
