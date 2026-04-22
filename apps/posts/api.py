from rest_framework import viewsets, permissions
from drf_spectacular.utils import extend_schema
from .models import Post
from .serializers import PostSerializer
from .permissions import IsOwnerOrReadOnly

@extend_schema(tags=['Posts'])
class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    queryset = Post.objects.all().select_related('user').prefetch_related('hashtags').order_by('-created_at')
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), IsOwnerOrReadOnly()]
        return [permissions.IsAuthenticated()]

    def perform_create(self, serializer):
        # Automatically link the post to the authenticated user
        serializer.save(user=self.request.user)