from django.contrib.auth.models import AbstractUser
from django.db import models


GENDER_CHOICES = (
    ("M", "Male"),
    ("F", "Female"),
)


class User(AbstractUser):
    address = models.TextField(blank=True, null=True)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    date_joined = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    first_name = models.CharField(max_length=25, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(blank=True, null=True)
    last_name = models.CharField(max_length=25, blank=True, null=True)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, blank=True, null=True)
    username = models.CharField(max_length=25, unique=True)




