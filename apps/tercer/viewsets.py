from rest_framework import viewsets
from .serializers import TercerSerializer
from .models import Tercer

class TercerViewSet(viewsets.ModelViewSet):
    serializer_class = TercerSerializer
    queryset = Tercer.objects.all()

