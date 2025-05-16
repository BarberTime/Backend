from rest_framework import viewsets
from .models import Pago
from .serializer import PagoSerializer

class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer   
