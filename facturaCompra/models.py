from django.db import models
from proveedores.models import Proveedor
from django.utils import timezone
from productos.models import Producto

class facturaCompra(models.Model):
    idFacturaCompra = models.BigAutoField(primary_key=True)
    idProveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, verbose_name="Nombre del proveedor")
    fecha = models.DateTimeField(default=timezone.now)
    total = models.DecimalField(max_digits=10,decimal_places=2)
    
    class Meta:
        verbose_name = "Factura de compra"
        verbose_name_plural = "Facturas de compra"
    
class facturaCompraContieneProductos(models.Model):
    idProducto = models.ForeignKey(Producto, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Nombre del producto")
    idFacturaCompra = models.ForeignKey(facturaCompra, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10,decimal_places=2)
    cantidad = models.IntegerField()
    descuento = models.DecimalField(max_digits=10,decimal_places=2)  

    class Meta:
        verbose_name = "Factura de compra contiene productos"
        verbose_name_plural = "Facturas de compra contiene productos"
  