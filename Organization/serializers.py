from rest_framework import serializers
from .models import Org, Proj

class OrgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Org 
        fields = ['name']

class ProjSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proj 
        fields = ['name', 'org']