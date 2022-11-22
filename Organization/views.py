from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
# from django.views.decorators import csrf_exempt
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Org, Proj
from User.models import User
from .serializers import OrgSerializer, ProjSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})

# class dummy(viewsets.ViewSet):
    
#     def list(self, request):
#         return Response("something!")



class AllOrgs(viewsets.ViewSet):

    def list(self, request):

        return Response(OrgSerializer(Org.objects.all(), many = True).data)


class AllProjs(viewsets.ViewSet):
    
    def list(self, request):

        return Response(ProjSerializer(Proj.objects.all(), many = True).data)

def AssignUser(request):
    # Logic
    pass