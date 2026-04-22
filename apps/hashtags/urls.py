from django.urls import path, include

from .api import HashtagViewSet
from rest_framework.routers import DefaultRouter


hashtag_router = DefaultRouter()


hashtag_router.register('hashtags', HashtagViewSet, basename='hashtags')



