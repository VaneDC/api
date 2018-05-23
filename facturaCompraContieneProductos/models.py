from django.db import models
from facturaCompra.models import facturaCompra
from productos.models import Producto

class facturaCompraContieneProductos(models.Model):
    idProducto = models.ForeignKey(Producto, on_delete=models.PROTECT, null=True, blank=True)
    idFacturaCompra = models.ForeignKey(facturaCompra, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10,decimal_places=2)
    cantidad = models.IntegerField()
    descuento = models.DecimalField(max_digits=10,decimal_places=2)
