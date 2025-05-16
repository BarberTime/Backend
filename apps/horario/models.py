
from django.db import models
import uuid
from apps.negocio.models import Negocio

class Horario(models.Model):
    DIAS_SEMANA = (
        (1, 'Lunes'),
        (2, 'Martes'),
        (3, 'Miércoles'), 
        (4, 'Jueves'),
        (5, 'Viernes'),
        (6, 'Sábado'),
        (7, 'Domingo'),
    )

    id_horario = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    negocio = models.ForeignKey(Negocio, on_delete=models.CASCADE)
    dia_semana = models.IntegerField(choices=DIAS_SEMANA)
    hora_apertura = models.TimeField()
    hora_cierre = models.TimeField()
    disponible = models.BooleanField(default=True)

    class Meta:
        db_table = 'horario'
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'

    def __str__(self):
        return f'{self.negocio} : {self.hora_apertura} a {self.hora_cierre}'


