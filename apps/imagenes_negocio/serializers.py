from rest_framework import serializers
from .models import ImagenNegocio
from apps.negocio.serializers import NegocioSerializer

class ImagenNegocioSerializer(serializers.ModelSerializer):
    negocio = NegocioSerializer(read_only=True)
    negocio_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Negocio.objects.all(), source='negocio')

    class Meta:
        model = ImagenNegocio
        fields = ['id_imagen', 'negocio', 'negocio_id', 'imagen', 'descripcion', 'es_principal', 'orden', 'fecha_subida']
        extra_kwargs = {
            'imagen': {'required': False},
            'negocio': {'required': True},
            'orden': {'required': True}
        }

    def create(self, validated_data):
        imagen = validated_data.pop('imagen', None)
        imagen_negocio = ImagenNegocio.objects.create(**validated_data)
        if imagen:
            imagen_negocio.imagen = imagen
            imagen_negocio.save()
        return imagen_negocio

    def update(self, instance, validated_data):
        imagen = validated_data.pop('imagen', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if imagen:
            instance.imagen = imagen
        instance.save()
        return instance
