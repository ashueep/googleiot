from rest_framework import serializers
from .models import VirtualDevice, Registry

class VDSerializer(serializers.ModelSerializer):
    class Meta:
        model = VirtualDevice
        fields = [
            'name', 
            'registry',
            'temp',
            'heater',
            'blood_sugar',
        ]

class RegistrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Registry
        fields = [
            'name',
            'proj',
        ]
