from django.db import models

# Create your models here.
class TipoDeVenta(models.Model):
    idTipoDeVenta = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = "Tipo de venta"
        verbose_name_plural = "Tipos de venta"

    def __str__(self):
        return self.nombre