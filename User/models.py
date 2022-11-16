from django.db import models
from django.contrib.auth.models import AbstractUser

from Organization.models import Org, Proj

# Create your models here.
class User(AbstractUser):

    dob = models.DateField(null=True)
    org = models.ForeignKey(Org, on_delete=models.CASCADE, null=True)
    projs = models.ManyToManyField(Proj, related_name='users', blank=True)

