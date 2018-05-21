from django.conf.urls import include, url
from . import views

app_name = "facturaCompra"

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^nuevo/$', views.nuevaFacturaCompra, name="nuevo"),
]