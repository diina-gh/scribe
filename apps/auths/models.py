from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    day_of_birth = models.IntegerField(null=True)
    month_of_birth = models.IntegerField(null=True)
    bio = models.TextField(blank=True)