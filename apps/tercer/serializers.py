from rest_framework import serializers
from .models import Tercer

class TercerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tercer
        fields = ( 'id', 'nom', 'cognom1', 'cognom2', 'correu', 'tipus' )

