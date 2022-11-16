from django.db import models
# from User.models import User
# Create your models here.

class Org(models.Model):
    name = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        permissions = ( 
                        ("add_user", "can add user to organization"),
                        ("remove_user", "can remove user from organization"),
                        ("assign_manager", "can assign prog_manager role to user"),
                    )

    
    def __str__(self) -> str:
        return self.name


class Proj(models.Model):
    name = models.CharField(max_length=255)
    org = models.ForeignKey(Org, on_delete=models.CASCADE, null=False)

    class Meta:
        permissions = ( 
                        ("add_user", "can add user to project in same organization"),
                        ("remove_user", "can remove user from project"),
                    )

    def __str__(self) -> str:
        return self.org.name + ' - ' + self.name