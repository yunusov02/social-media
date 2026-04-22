from django.urls import path, include

from rest_framework import routers

from .api import UserProfileView, LoginView, LogoutView, PasswordChangeView, RegisterView

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    path('auth/password-change/', PasswordChangeView.as_view(), name='password-change'),
    path('auth/profile/', UserProfileView.as_view(), name='user-profile'),
]
