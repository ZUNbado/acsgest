from rest_framework import viewsets
from .serializers import ContracteSerializer
from .models import Contracte

class ContracteViewSet(viewsets.ModelViewSet):
    serializer_class = ContracteSerializer
    queryset = Contracte.objects.all()

