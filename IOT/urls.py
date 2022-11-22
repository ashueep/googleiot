from django.urls import include, path
from rest_framework import routers
from .views import AssignVDtoReg

routers = routers.DefaultRouter()

urlpatterns = [
    path('assign-to-reg/', AssignVDtoReg, name = 'assign to registry')
]

# routers.register('assign-to-reg', )