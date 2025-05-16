from rest_framework import viewsets
from .models import Horario
from .serializer import HorarioSerializer                       

class HorarioViewSet(viewsets.ModelViewSet):
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer
    