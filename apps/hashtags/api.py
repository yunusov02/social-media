from rest_framework import viewsets
from .models import Hashtags
from .serializer import HashtagSerializer


class HashtagViewSet(viewsets.ModelViewSet):
    queryset = Hashtags.objects.all()
    serializer_class = HashtagSerializer


