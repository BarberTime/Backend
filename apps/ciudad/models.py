from django.db import models
import uuid
# Create your models here.

class Ciudad(models.Model):
    id_ciudad = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)

    class Meta:
        db_table = 'ciudad'

    def __str__(self):
        return self.nombre
