from django.db import models
import uuid
from apps.usuario.models import Usuario
from apps.negocio.models import Negocio
from apps.cita.models import Cita

class Resenia(models.Model):
    id_resenia = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cliente = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    negocio = models.ForeignKey(Negocio, on_delete=models.CASCADE)
    cita_id = models.ForeignKey(Cita, on_delete=models.SET_NULL, null=True)
    calificacion = models.IntegerField()  # Valor esperado entre 1 y 5
    comentario = models.TextField(blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'resenia'

    def __str__(self):
        return f'Reseña {self.id} - {self.cliente_id} - {self.negocio_id}'
