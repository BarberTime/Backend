from rest_framework import serializers
from .models import Ciudad

class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = ['id_ciudad', 'nombre', 'pais']
        extra_kwargs = {
            'nombre': {'required': True},
            'pais': {'required': True}
        }
