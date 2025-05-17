from rest_framework import serializers
from .models import Usuario
from apps.rol.models import Rol

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id_usuario', 'id_rol', 'nombre', 'apellido', 'email', 
                  'telefono', 'password_hash', 'foto_perfil', 'fecha_registro']
        extra_kwargs = {
            'password_hash': {'write_only': True},
            'foto_perfil': {'required': False},
            'id_rol': {'required': True},
            'nombre': {'required': True},
            'apellido': {'required': True},
            'email': {'required': True},
            'password_hash': {'required': True}
        }

    def create(self, validated_data):
        foto_perfil = validated_data.pop('foto_perfil', None)
        usuario = Usuario.objects.create(**validated_data)
        if foto_perfil:
            usuario.foto_perfil = foto_perfil
            usuario.save()
        return usuario

    def update(self, instance, validated_data):
        foto_perfil = validated_data.pop('foto_perfil', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if foto_perfil:
            instance.foto_perfil = foto_perfil
        instance.save()
        return instance
