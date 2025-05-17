from django.db import models
import uuid
from apps.negocio.models import Negocio
from apps.categoria.models import Categoria
from cloudinary.models import CloudinaryField

# Create your models here.

class Servicio(models.Model):
    id_servicio = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    negocio = models.ForeignKey(Negocio, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    duracion_minutos = models.IntegerField()
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'servicio'

    def __str__(self):
        return f'{self.nombre} - {self.negocio_id}'

class ImagenServicio(models.Model):
    id_imagen = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE, related_name='imagenes')
    imagen = CloudinaryField('imagen', folder='servicios', blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    es_principal = models.BooleanField(default=False)
    orden = models.IntegerField()
    fecha_subida = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'imagenes_servicio'
        ordering = ['orden']

    def __str__(self):
        return f"Imagen {self.id_imagen} - {self.servicio}"

