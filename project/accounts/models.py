from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class Profile(models.Model):
    introduction = models.CharField(max_length = 1000, blank = True, null = True)
    avatar = models.ImageField(upload_to = 'images/', blank = True, null = True)
    is_visable = models.BooleanField(default = False)
    user = models.OneToOneField(User, on_delete = models.CASCADE)
















