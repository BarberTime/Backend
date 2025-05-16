from django.db import models

class MetodoPago(models.Model):
    id_metodo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, choices=[
        ('QR', 'QR'),
        ('Tarjeta', 'Tarjeta')
    ])
    descripcion = models.TextField(null=True, blank=True)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = 'metodos_pago'

    def __str__(self):
        return self.nombre


