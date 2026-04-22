from rest_framework.routers import DefaultRouter
from .api import PostViewSet

post_router = DefaultRouter()
post_router.register('posts', PostViewSet, basename='posts')

urlpatterns = []