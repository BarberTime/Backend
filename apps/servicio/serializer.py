from rest_framework import serializers
from .models import Servicio, ImagenServicio

class ImagenServicioSerializer(serializers.ModelSerializer):
    imagen_url = serializers.SerializerMethodField()
    
    class Meta:
        model = ImagenServicio
        fields = ['id_imagen', 'servicio', 'imagen', 'imagen_url', 'descripcion', 'es_principal', 'orden', 'fecha_subida']

    def get_imagen_url(self, obj):
        if obj.imagen:
            return obj.imagen.url
        return None

class ServicioSerializer(serializers.ModelSerializer):
    imagenes = ImagenServicioSerializer(many=True, read_only=True)

    class Meta:
        model = Servicio
        fields = ['id_servicio', 'negocio', 'categoria', 'nombre', 'descripcion', 'precio', 'duracion_minutos', 'activo', 'fecha_creacion', 'fecha_actualizacion', 'imagenes']
