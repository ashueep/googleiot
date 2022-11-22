from django.contrib import admin
from .models import VirtualDevice, Registry

# Register your models here.
admin.site.register(VirtualDevice)
admin.site.register(Registry)