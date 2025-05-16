from django.db import models    
import uuid
from apps.cliente.models import Cliente
from apps.negocio.models import Negocio
from apps.servicio.models import Servicio
from apps.empleados.models import Empleado

# Create your models here.
class Cita(models.Model):
    id_cita = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cliente= models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    negocio = models.ForeignKey(Negocio, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.SET_NULL, null=True)
    empleado = models.ForeignKey(Empleado, on_delete=models.SET_NULL, null=True, related_name='citas_empleado')
    fecha_hora = models.DateTimeField()
    estado = models.CharField(max_length=20, choices=[
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'), 
        ('completada', 'Completada'),
        ('cancelada', 'Cancelada')
    ])
    precio_final = models.DecimalField(max_digits=10, decimal_places=2)
    notas = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = 'cita'

    def __str__(self):
        return f'Cita {self.id} - {self.cliente} - {self.fecha_hora}'
