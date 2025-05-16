from rest_framework import serializers
from .models import ImagenNegocio

class ImagenNegocioSerializer(serializers.ModelSerializer):
    imagen_url = serializers.SerializerMethodField()
    
    class Meta:
        model = ImagenNegocio
        fields = ['id_imagen', 'negocio', 'imagen', 'imagen_url', 'descripcion', 'es_principal', 'orden', 'fecha_subida']

    def get_imagen_url(self, obj):
        if obj.imagen:
            return obj.imagen.url
        return None 
