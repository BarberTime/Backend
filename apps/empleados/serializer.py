from rest_framework import serializers
from .models import Empleado

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ['id_empleado', 'negocio', 'nombre', 'apellidos', 'email', 'telefono', 'foto', 'biografia', 'especialidad', 'fecha_contratacion', 'estado']
