from django.db import models

# Create your models here.
class MedioDePago(models.Model):
    idMedioDePago = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = "Medio de pago"
        verbose_name_plural = "Medios de pago"

    def __str__(self):
        return self.nombre
