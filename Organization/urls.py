from rest_framework import routers
from django.urls import path, include
from .views import AllOrgs, hello_world, AllProjs, AssignRoleManager, AssignProject

routers = routers.SimpleRouter()

# routers.register(r'all', AllOrgs, basename='all-orgs')
# routers.register(r'dummy', hello_world, basename='dummy')
routers.register(r'all', AllOrgs, basename='all-orgs')
routers.register(r'projs', AllProjs, basename='all-projs')

print("routers = " + str(routers.urls))

urlpatterns = [
    path('dummy/', hello_world, name = 'hello-world'),
    path('assign-manager/', AssignRoleManager, name = 'assign-manager'),
    path('assign-project/', AssignProject, name = 'assign-project')
]

urlpatterns += routers.urls
