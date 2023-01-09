from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_comissaire = models.BooleanField(default=False)
    is_president = models.BooleanField(default=False)
    is_secretaire = models.BooleanField(default=False)
    is_membre = models.BooleanField(default=True)