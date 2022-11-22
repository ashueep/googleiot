from django.shortcuts import render

from django.http import HttpRequest

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import VirtualDevice, Registry
from .serializers import VDSerializer, RegistrySerializer

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from User.models import User
from rest_framework.decorators import authentication_classes, permission_classes

# Create your views here.

@api_view(['POST'])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated])
def AssignVDtoReg(request):
    if request.method == 'POST':
        username = request.data['username']
        user = User.objects.get(username=username)

        if user.groups.filter(name = 'provisioner'):

            vd = VirtualDevice.objects.get(id=request.data['vd'])
            reg = Registry.objects.get(id=request.data['reg'])
            if user.projs.filter(name = reg.proj.name):
            
                vd.registry = reg
                print(vd)
                vd.save()
                return Response(VDSerializer(vd).data)
            
            else:
                return Response(status=401)

        else:
            return Response(status=401)

@api_view(['POST'])
def BodySensor(request):
    if request.method == 'POST':
        vd = VirtualDevice.objects.get(id=request.data['vd'])

        if vd.temp > 32:
            print('logging to database.....')
            print('sending notification to doctors....')

            return Response("alert to docs sent, approaching soon!")

@api_view(['POST'])
def RoomSensor(request):
    if request.method == 'POST':
        vd = VirtualDevice.objects.get(id=request.data(['vd']))

        if vd.temp > 27:
            vd.heater = False
            vd.save()

            return Response("lowering temprature....")

        if vd.temp < 18:
            vd.heater = True
            vd.save()

            return Response("increasing temprature...")
