from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Club(models.Model):
    name = models.CharField(max_length = 20)
    introduction = models.CharField(max_length = 500)
    cover = models.ImageField(upload_to = 'images/club/', blank = True, null = True)
    user = models.ManyToManyField(User)
    admin = models.ForeignKey(User, on_delete = models.CASCADE, related_name='club_admin')

   
