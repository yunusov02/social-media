from django.contrib import admin

# Register your models here.
from .models import User, UserProfile


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile Information'
    fk_name = 'user'


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email']
    list_display_links = ['id', 'username', 'email']
    search_fields = ['username', 'email']
    ordering = ['username']
    inlines = [UserProfileInline]
