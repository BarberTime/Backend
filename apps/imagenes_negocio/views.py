from rest_framework import viewsets 
from .models import ImagenNegocio
from .serializer import ImagenNegocioSerializer

class ImagenNegocioViewSet(viewsets.ModelViewSet):
    queryset = ImagenNegocio.objects.all()
    serializer_class = ImagenNegocioSerializer

    