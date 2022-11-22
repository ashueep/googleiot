"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from .router import router
# from rest_framework_jwt.views import obtain_jwt_token

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )
from rest_framework.authtoken import views

from User.views import LoginView, User_logout

urlpatterns = [
    path('api/orgs/', include('Organization.urls')),
    path('api/iot/', include('IOT.urls')),
    path('admin/', admin.site.urls),
    path('api/login/', LoginView.as_view()),
    path('logout/', User_logout)
    # path('api/login/', CustomAuthToken.as_view()),

    # path('login/', LoginAPI.as_view()),
    # path(r'^token/', obtain_jwt_token),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/', include(router.urls)),
]

print("urls in src = " + str(urlpatterns))
