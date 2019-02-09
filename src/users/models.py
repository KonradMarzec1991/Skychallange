from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class MyUser(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(unique=True)
    is_lecturer = models.BooleanField(default=False) # Required attribute to permissions

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.email
