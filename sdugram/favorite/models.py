from django.db import models
from django.contrib.auth.models import User
from grid_panel.models import Advt


# Create your models here.
class Favorites(models.Model):
    users = models.ManyToManyField(User)
    advt = models.IntegerField()
    class Meta:
        verbose_name_plural = "Favorites"
        verbose_name = "Favorite"