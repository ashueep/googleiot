from rest_framework import serializers
from .models import Org, Proj

class OrgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Org 
        fields = ['id', 
        'name', 
        'created_on'
        ]

class ProjSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proj 
        fields = ['id', 
        'name', 
        'org'
        ]