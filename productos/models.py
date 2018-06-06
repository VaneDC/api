from django.db import models

class Producto(models.Model):
    idProducto = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=300)
    stock = models.SmallIntegerField()
    stock_minimo = models.SmallIntegerField()
    costo = models.DecimalField(max_digits=10,decimal_places=2)
    precio_minorista = models.DecimalField(max_digits=10,decimal_places=2)
    precio_mayorista = models.DecimalField(max_digits=10,decimal_places=2)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    # metodo string que devuelve el titulo
    def __str__(self):
        return self.nombre
