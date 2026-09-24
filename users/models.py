from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Пользователь."""

    username = None
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to="users/", blank=True, null=True)
    phone = models.CharField(max_length=35, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
