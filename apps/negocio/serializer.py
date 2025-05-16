from rest_framework import serializers
from .models import Negocio

class NegocioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Negocio
        fields = [
            'id_negocio',
            'propietario',
            'ciudad',
            'nombre',
            'descripcion',
            'direccion',
            'latitud',
            'longitud',
            'telefono',
            'email',
            'sitio_web',
            'logo',
            'fotos',
            'calificacion_promedio',        
            'verificado',
            'fecha_registro',
        ]
