from rest_framework import viewsets
from .models import Ciudad
from .serializer import CiudadSerializer

class CiudadViewSet(viewsets.ModelViewSet):
    queryset = Ciudad.objects.all()
    serializer_class = CiudadSerializer

# Create your views here.
            