from django.db import models
import uuid
# Create your models here.

class Rol(models.Model):
    id_rol = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        db_table = 'roles'

    def __str__(self):
        return f'Rol: {self.nombre}'
