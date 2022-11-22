from django.db import models

from Organization.models import Org, Proj



# Create your models here.
# class CloudFunction(models.Model):
#     name = models.CharField()
#     to_manager = models.CharField()
#     to_device = models.CharField()
#     to_store = models.CharField()

#     class Meta:
#         permissions = (
#             ("notify_manager", "sends notification to manager"),
#             ("notify_device", "sends notification back to device"),
#             ("store", "store information in database"),
#             )

class Registry(models.Model):
    name = models.CharField(max_length=255)
    proj = models.ForeignKey(Proj, on_delete=models.CASCADE)
    # function = models.ForeignKey(CloudFunction)

    def __str__(self) -> str:
        return self.name

class VirtualDevice(models.Model):
    name = models.CharField(max_length=255)
    registry = models.ForeignKey(to=Registry, related_name='vds', on_delete=models.CASCADE, blank = True, null = True)

    class Meta:
        permissions = (
            ('assign_device', 'assigns device to registry'),
        )

    temp = models.IntegerField(default=0, blank=True)
    blood_sugar = models.FloatField(default=0, blank=True)
    heater = models.BooleanField(default=0, blank=True)

    def __str__(self) -> str:
        if self.registry is None:
            return self.name
        return self.registry.name + ' - ' + self.name



