from rest_framework import serializers
from .models import Servicio, ImagenServicio
from apps.negocio.serializers import NegocioSerializer
from apps.categoria.serializers import CategoriaSerializer

class ImagenServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenServicio
        fields = ['id_imagen', 'servicio', 'imagen', 'descripcion']
        extra_kwargs = {
            'imagen': {'required': False},
            'servicio': {'required': True}
        }

    def create(self, validated_data):
        imagen = validated_data.pop('imagen', None)
        imagen_servicio = ImagenServicio.objects.create(**validated_data)
        if imagen:
            imagen_servicio.imagen = imagen
            imagen_servicio.save()
        return imagen_servicio

    def update(self, instance, validated_data):
        imagen = validated_data.pop('imagen', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if imagen:
            instance.imagen = imagen
        instance.save()
        return instance

class ServicioSerializer(serializers.ModelSerializer):
    negocio = NegocioSerializer(read_only=True)
    categoria = CategoriaSerializer(read_only=True)
    negocio_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Negocio.objects.all(), source='negocio')
    categoria_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Categoria.objects.all(), source='categoria')
    imagenes = ImagenServicioSerializer(many=True, read_only=True)

    class Meta:
        model = Servicio
        fields = ['id_servicio', 'negocio', 'negocio_id', 'categoria', 'categoria_id', 'nombre', 'descripcion', 
                  'precio', 'duracion_minutos', 'activo', 'fecha_creacion', 'fecha_actualizacion', 'imagenes']
        extra_kwargs = {
            'negocio': {'required': True},
            'nombre': {'required': True},
            'precio': {'required': True},
            'duracion_minutos': {'required': True}
        }

    def create(self, validated_data):
        servicio = Servicio.objects.create(**validated_data)
        return servicio

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
