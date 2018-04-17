from django.db import models
from factura.models import Factura

class facturaCompra(models.Model):
    idFacturaCompra = models.BigAutoField(primary_key=True)
    idFactura = models.OneToOneField(Factura, on_delete = models.CASCADE)
