from rest_framework import viewsets
from .serializers import CaixaSerializer
from .models import Caixa

class CaixaViewSet(viewsets.ModelViewSet):
    serializer_class = CaixaSerializer
    queryset = Caixa.objects.all()

