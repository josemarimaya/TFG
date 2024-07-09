from django.test import TestCase

# Other imports 

from django.db import models
from django.contrib.auth.models import User

# Create your tests here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialties = models.TextField(blank=True)  # Campo de especialidades

    def __str__(self):
        return f'{self.user.username} Profile'

