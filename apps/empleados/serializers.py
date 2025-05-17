from rest_framework import serializers
from .models import Empleado
from apps.negocio.serializers import NegocioSerializer

class EmpleadoSerializer(serializers.ModelSerializer):
    negocio = NegocioSerializer(read_only=True)
    negocio_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Negocio.objects.all(), source='negocio')

    class Meta:
        model = Empleado
        fields = ['id_empleado', 'negocio', 'negocio_id', 'nombre', 'apellidos', 'email', 
                  'telefono', 'foto', 'biografia', 'especialidad', 'fecha_contratacion', 
                  'estado', 'fecha_creacion']
        extra_kwargs = {
            'foto': {'required': False},
            'email': {'required': False},
            'telefono': {'required': False},
            'biografia': {'required': False},
            'especialidad': {'required': False},
            'negocio': {'required': True},
            'nombre': {'required': True},
            'apellidos': {'required': True},
            'fecha_contratacion': {'required': True}
        }

    def create(self, validated_data):
        foto = validated_data.pop('foto', None)
        empleado = Empleado.objects.create(**validated_data)
        if foto:
            empleado.foto = foto
            empleado.save()
        return empleado

    def update(self, instance, validated_data):
        foto = validated_data.pop('foto', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if foto:
            instance.foto = foto
        instance.save()
        return instance
