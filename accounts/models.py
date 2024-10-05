from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    address = models.TextField(null=True, blank=True)
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    
    GENDERS = (
        ("M", "Male"),
        ("F", "Female"),
    )
    gender = models.CharField(choices=GENDERS, max_length=1, blank=True, null=True)

    def __str__(self):
        return self.username
