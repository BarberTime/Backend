from rest_framework import viewsets
from .models import Resenia
from .serializer import ReseniaSerializer

class ReseniaViewSet(viewsets.ModelViewSet):
    queryset = Resenia.objects.all()
    serializer_class = ReseniaSerializer

# Create your views here.
