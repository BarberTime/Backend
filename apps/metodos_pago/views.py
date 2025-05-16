from rest_framework import viewsets
from .models import MetodoPago
from .serializer import MetodoPagoSerializer

class MetodoPagoViewSet(viewsets.ModelViewSet):
    queryset = MetodoPago.objects.all()
    serializer_class = MetodoPagoSerializer
