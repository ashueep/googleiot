from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager, PermissionsMixin

from Organization.models import Org, Proj

# Create your models here.

# class CustUserManager(BaseUserManager):
# 	def create_user(self, userName, email, firstName, mobileNumber, password = None):
# 		if not userName:
# 			raise ValueError('User must have username')

# 		if not email:
# 			raise ValueError('User must have email')

# 		user = self.model(userName = userName, email = self.normalize_email(email), firstName = firstName, mobileNumber = mobileNumber,)

# 		user.set_password(password)
# 		user.save(using = self._db)

# 		return user

# 	def create_superuser(self, userName, email, firstName, mobileNumber, password = None):
# 		user = self.create_user(userName, email, firstName, mobileNumber, password)
		
# 		user.is_admin = True
# 		user.save(using = self._db)

# 		return user

# class User(AbstractBaseUser):
# 	userName         = models.CharField(verbose_name = 'Username', max_length = 27, unique = True)
# 	email            = models.CharField(verbose_name = 'Email Address', max_length = 27, unique = True)
# 	firstName        = models.CharField(verbose_name = 'First Name',max_length = 27)
# 	lastName         = models.CharField(verbose_name = 'Last Name' ,max_length = 27, null = True)
# 	org              = models.ForeignKey(Org, on_delete=models.CASCADE, null=True)
# 	projs            = models.ManyToManyField(Proj, related_name='users', blank=True)
# 	is_active        = models.BooleanField(default = True)
# 	is_admin         = models.BooleanField(default = False)

# 	objects = CustUserManager()

# 	USERNAME_FIELD  = 'userName'
# 	REQUIRED_FIELDS = ['email', 'firstName', 'org', ]

# 	def __str__(self):
# 		return self.userName

# 	def has_perm(self, perm, obj = None):
# 		return True

# 	def has_module_perms(self,app_label):
# 		return True

# 	@property
# 	def is_staff(self):
# 		return self.is_admin

class User(AbstractUser):

    dob = models.DateField(null=True)
    org = models.ForeignKey(Org, on_delete=models.CASCADE, null=True)
    projs = models.ManyToManyField(Proj, related_name='users', blank=True)

