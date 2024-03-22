from django.db import models
from django.contrib.auth.models import AbstractUser
  


class CustomUser(AbstractUser):
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=128)
    messgae = models.TextField(max_length=300)