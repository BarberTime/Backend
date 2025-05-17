from rest_framework import serializers
from .models import Negocio
from apps.usuario.serializers import UsuarioSerializer
from apps.ciudad.serializers import CiudadSerializer
from apps.ciudad.models import Ciudad

class NegocioSerializer(serializers.ModelSerializer):
    propietario = UsuarioSerializer(read_only=True)
    ciudad = CiudadSerializer(read_only=True)
    ciudad_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Ciudad.objects.all(), source='ciudad')
    propietario_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Usuario.objects.all(), source='propietario')

    class Meta:
        model = Negocio
        fields = ['id_negocio', 'propietario', 'propietario_id', 'ciudad', 'ciudad_id', 'nombre', 'descripcion', 
                  'direccion', 'latitud', 'longitud', 'telefono', 'email', 'sitio_web', 'logo', 'fotos', 
                  'calificacion_promedio', 'verificado', 'fecha_registro']
        extra_kwargs = {
            'logo': {'required': False},
            'fotos': {'required': False},
            'ciudad': {'required': True},
            'nombre': {'required': True},
            'direccion': {'required': True},
            'propietario': {'required': True}
        }

    def create(self, validated_data):
        logo = validated_data.pop('logo', None)
        fotos = validated_data.pop('fotos', None)
        negocio = Negocio.objects.create(**validated_data)
        if logo:
            negocio.logo = logo
        if fotos:
            negocio.fotos = fotos
        negocio.save()
        return negocio

    def update(self, instance, validated_data):
        logo = validated_data.pop('logo', None)
        fotos = validated_data.pop('fotos', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if logo:
            instance.logo = logo
        if fotos:
            instance.fotos = fotos
        instance.save()
        return instance
