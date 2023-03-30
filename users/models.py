from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from .managers import AppUserManager


class AppUser(AbstractBaseUser, PermissionsMixin):
    AUTHOR = "AUT"
    READER = "RDR"

    ROLE_CHOICES = [
        (AUTHOR, 'Author'),
        (READER, 'Reader'),
    ]

    firstname = models.CharField(max_length=150, null=True, blank=True, default=None)
    lastname = models.CharField(max_length=150, null=True, blank=True, default=None)
    email = models.EmailField("email address", unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    role = models.CharField(
        max_length=3,
        choices=ROLE_CHOICES,
        default=READER,
    )
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = AppUserManager()

    def __str__(self):
        return f"{self.role}: {self.email}"
