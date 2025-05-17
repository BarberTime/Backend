from django.db import models
import uuid
from apps.usuario.models import Usuario
# Create your models here.
class AuthLogin(models.Model):
    id_auth_login = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'auth_login'
    
    def __str__(self):
        return self.email