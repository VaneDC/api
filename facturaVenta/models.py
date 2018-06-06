from django.db import models
from django.utils import timezone
#importo modelos
from mediosDePago.models import MedioDePago
from tiposDeVenta.models import TipoDeVenta
from productos.models import Producto

# Create your models here.
class facturaVenta(models.Model):
    idFacturaVenta = models.BigAutoField(primary_key=True)
    idMedioDePago = models.ForeignKey(MedioDePago, on_delete=models.CASCADE, verbose_name="Medio de pago")
    idTipoDeVenta = models.ForeignKey(TipoDeVenta, on_delete=models.CASCADE, verbose_name="tipo de venta")
    fecha = models.DateTimeField(default=timezone.now)
    total = models.DecimalField(max_digits=10,decimal_places=2)
    
    class Meta:
        verbose_name = "Factura de venta"
        verbose_name_plural = "Facturas de venta"

class facturaVentaContieneProductos(models.Model):
    idProducto = models.ForeignKey(Producto, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Producto")
    idfacturaVenta = models.ForeignKey(facturaVenta, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10,decimal_places=2)
    cantidad = models.IntegerField()
    descuento = models.DecimalField(max_digits=10,decimal_places=2)  

    class Meta:
        verbose_name = "Factura de venta contiene productos"
        verbose_name_plural = "Facturas de venta contiene productos"