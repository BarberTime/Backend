from django.db import models
from apps.cita.models import Cita
from apps.metodos_pago.models import MetodoPago
    
# Create your models here
class Pago(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('completado', 'Completado'), 
        ('reembolsado', 'Reembolsado')
    ]

    id_pago = models.AutoField(primary_key=True)
    id_cita = models.ForeignKey(Cita, on_delete=models.CASCADE)
    id_metodo = models.ForeignKey(MetodoPago, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=50, choices=ESTADO_CHOICES)
    referencia = models.CharField(max_length=100, blank=True, null=True)
    fecha_pago = models.DateTimeField(null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        db_table = 'pagos'

    def __str__(self):
        return f'Pago {self.id_pago} - {self.estado}'
