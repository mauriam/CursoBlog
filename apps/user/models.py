from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    full_name =  models.CharField(max_length=255)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    photo = models.ImageField(blank=True,null=True)
    