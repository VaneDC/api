from django.db import models
from proveedores.models import Proveedor 
from django.utils import timezone

class facturaCompra(models.Model):
    idFacturaCompra = models.BigAutoField(primary_key=True)
    idProveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=timezone.now)
    total = models.FloatField()