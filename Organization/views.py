from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
# from django.views.decorators import csrf_exempt
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Org, Proj
from User.models import User
from .serializers import OrgSerializer, ProjSerializer
from django.contrib.auth.models import Group
from rest_framework import status, permissions
# Create your views here.

@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})

# class dummy(viewsets.ViewSet):
    
#     def list(self, request):
#         return Response("something!")
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def AssignRoleManager(request):
    if request.method == "POST":
        exec = request.user
        manager = User.objects.get(username=request.data['user'])
        if exec.org != manager.org or not exec.groups.filter(name = 'org_exec').exists():
            print('Failed')
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        role = Group.objects.get(name='proj_manager')
        manager.groups.add(role)
        return Response({
            "username" : manager.username,
        }, status=status.HTTP_201_CREATED)
    return Response()


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def AssignProject(request):
    if request.method == "POST":
        print(request.data)
        exec = request.user
        emp = User.objects.get(username=request.data['user'])
        proj = Proj.objects.get(id=request.data['proj'])
        if exec.org != emp.org and proj.org != exec.org:
            print('Failed')
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        if_exec = exec.groups.filter(name = 'org_exec').exists()
        if_manager = exec.groups.filter(name = 'proj_manager').exists()
        if if_exec or if_manager: 
            emp.projs.add(proj)
            emp.save()
        return Response({
            "username" : emp.username,
            "proj" : str(proj),
        }, status=status.HTTP_201_CREATED)
    return Response('invalid type')


class AllOrgs(viewsets.ViewSet):

    def list(self, request):

        return Response(OrgSerializer(Org.objects.all(), many = True).data)


class AllProjs(viewsets.ViewSet):
    
    def list(self, request):

        return Response(ProjSerializer(Proj.objects.all(), many = True).data)

def AssignUser(request):
    # Logic
    pass