from django.db import models
import uuid
from apps.negocio.models import Negocio
from django.core.files.storage import FileSystemStorage

def upload_to(instance, filename):
    return f'imagenes/{instance.negocio.nombre}/{filename}'

# Configuración del almacenamiento de archivos
fs = FileSystemStorage(location='media/')

class ImagenNegocio(models.Model):
    id_imagen = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    negocio = models.ForeignKey(Negocio, on_delete=models.CASCADE)
    imagen = models.FileField(storage=fs, upload_to=upload_to, null=True, blank=True)
    descripcion = models.CharField(max_length=255, null=True, blank=True)
    es_principal = models.BooleanField(default=False)
    orden = models.IntegerField()
    fecha_subida = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'imagenes_negocio'

    def __str__(self):
        return f"Imagen {self.id_imagen} - {self.negocio}"
