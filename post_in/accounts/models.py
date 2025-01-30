from django.db.models import (EmailField, CharField, BooleanField, DateTimeField, )
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager


class User(AbstractBaseUser):
    email = EmailField(unique=True, max_length=255)
    full_name = CharField(max_length=255, blank=True, null=True)
    is_staff = BooleanField(default=False)
    admin = BooleanField(default=False)
    timestamp = DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []