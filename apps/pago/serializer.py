from rest_framework import serializers
from .models import Pago

class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = ['id_pago', 'id_cita', 'id_metodo', 'monto', 'estado', 'referencia', 'fecha_pago']