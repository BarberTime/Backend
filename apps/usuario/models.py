from django.db import models
import uuid
from apps.rol.models import Rol
from cloudinary.models import CloudinaryField

# Create your models here.

class Usuario(models.Model):
    id_usuario = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE,default=1)
    nombre = models.CharField(max_length=100, null=True,)
    apellido = models.CharField(max_length=100, null=True,)
    email = models.EmailField(max_length=100, unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    password_hash = models.CharField(max_length=255)
    foto_perfil = CloudinaryField('foto_perfil', folder='usuarios', null=True, blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'usuario'

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

