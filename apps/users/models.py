from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from core.softdelete import SoftDeleteModel, SoftDeleteManager, SoftDeleteUserManager



"""

AbstractUser - Full User model with fields
    username
    email
    password
    first_name
    last_name
        

AbstractBaseUser - core functionality (password management)


"""

class User(SoftDeleteModel, AbstractBaseUser, PermissionsMixin):

    objects = SoftDeleteUserManager()
    all_objects = models.Manager()

    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    class Meta:

        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


    def __str__(self):
        return self.username
    
    # def get_full_name(self):
    #     # The user profile holds first_name and last_name, so we need to link them
    #     try:
    #         return f"{self.userprofile.first_name} {self.userprofile.last_name}"
    #     except UserProfile.DoesNotExist:
    #         return self.username

    # def get_short_name(self):
    #     try:
    #         return self.userprofile.first_name
    #     except UserProfile.DoesNotExist:
    #         return self.username

    



class UserProfile(SoftDeleteModel):

    objects = SoftDeleteManager()
    all_objects = models.Manager()

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_date = models.DateField(blank=True, null=True)
    location = models.CharField(blank=True, max_length=255)
    website = models.URLField(blank=True)
    lot = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)

    class Meta:

        db_table = 'user_profiles'
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

    def __str__(self):
        return self.user.username
    
