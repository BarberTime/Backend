from rest_framework import serializers
from .models import MetodoPago

class MetodoPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetodoPago
        fields = ['id_metodo', 'nombre', 'descripcion', 'activo']
