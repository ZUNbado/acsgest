from rest_framework import serializers
from .models import Contracte

class ContracteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contracte
        fields = ( 'id', 'tercer', 'serveis', 'periode', 'comentari', 'multi', 'descompte', 'alta', 'actiu', 'expired' )

