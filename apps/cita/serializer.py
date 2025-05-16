from rest_framework import serializers
from .models import Cita

class CitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cita
        fields = ['id_cita', 'cliente', 'negocio', 'servicio', 'empleado', 'fecha_hora', 'estado','precio_final']  
