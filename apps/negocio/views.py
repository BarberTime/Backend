from rest_framework import viewsets
from .models import Negocio
from .serializer import NegocioSerializer

class NegocioViewSet(viewsets.ModelViewSet):
    queryset = Negocio.objects.all()
    serializer_class = NegocioSerializer    
