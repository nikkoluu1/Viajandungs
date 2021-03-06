from rest_framework import serializers
from viajes.models import Viaje

class ViajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viaje
        fields = (
            'pk',
            'name',
            'description',
            'date',
            'createdAt'
        )