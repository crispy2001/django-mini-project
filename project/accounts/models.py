from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class Profile(models.Model):
    introduction = models.CharField(max_length = 1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default = 1)
















