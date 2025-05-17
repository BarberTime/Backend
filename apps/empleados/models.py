import uuid
from django.db import models
from apps.negocio.models import Negocio
from cloudinary.models import CloudinaryField

class Empleado(models.Model):
    id_empleado = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    negocio = models.ForeignKey(Negocio, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    foto = CloudinaryField('foto', folder='empleados', null=True, blank=True)
    biografia = models.TextField(null=True, blank=True)
    especialidad = models.CharField(max_length=100, null=True, blank=True)
    fecha_contratacion = models.DateField()
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'empleados'

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"
