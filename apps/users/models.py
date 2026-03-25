from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

"""
AbstractUser
AbstractBaseUser

Both of them used to create custom user models difference between level of control

AbstractUser
    - abstract model provides full implementation of the default django User Model
    - when to use: when you want to keep Django's default user fields (username email first_name, last_name is_staff is_active)
    - fields included by default
    - ease of use
    - customization: add new fields easily email address for authentication --> USERNAME_FIELD = 'email'

AbstractBaseUser
    - Minimal abstract base class that only contains the core authentication functionality and no other fields
    - when to use: when you need complete control over the user model and want redefine the user structure for phone_number for login
    - fields included by default: id, password, last_login
    - you must require all fields (username, email, is_active, etc.)

"""


class User(AbstractUser):
    pass

