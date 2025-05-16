from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    foto_perfil_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Usuario
        fields = ['id_usuario','id_rol', 'nombre', 'apellido', 'email', 'telefono', 'password_hash', 'foto_perfil', 'foto_perfil_url']

    def get_foto_perfil_url(self, obj):
        if obj.foto_perfil:
            return obj.foto_perfil.url
        return None
