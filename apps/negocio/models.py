from django.db import models
import uuid
from apps.usuario.models import Usuario
from apps.ciudad.models import Ciudad
from apps.core.utils import get_upload_path

# Create your models here.

class Negocio(models.Model):
    id_negocio = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    propietario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE,default=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    direccion = models.CharField(max_length=255)
    latitud = models.FloatField(null=True, blank=True)
    longitud = models.FloatField(null=True, blank=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    sitio_web = models.URLField(max_length=255, blank=True, null=True)
    logo = models.ImageField(upload_to=get_upload_path, blank=True, null=True)
    fotos = models.ImageField(upload_to=get_upload_path, blank=True, null=True)
    calificacion_promedio = models.FloatField(default=0)
    verificado = models.BooleanField(default=False)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'negocio'
        
    def __str__(self):
        return self.nombre

