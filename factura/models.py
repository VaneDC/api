from django.db import models

class Factura(models.Model):
    idFactura = models.BigAutoField(primary_key = True)
    fecha = models.DateTimeField(auto_now = True)
    total = models.FloatField()

 