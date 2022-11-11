from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from clubs.models import Club
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length = 20)
    article = models.CharField(max_length = 5000)
    is_visable = models.IntegerField(default = 0)
    # null tells database to accept null value
    create_time = models.TimeField(blank = True, null = True)
    update_time = models.TimeField(blank = True, null = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    club = models.ForeignKey(Club, on_delete = models.CASCADE, blank = True, null = True)

