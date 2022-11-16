from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Org, Proj
from .serializers import OrgSerializer, ProjSerializer

# Create your views here.


def AssignUser(request):
    # Logic
    pass