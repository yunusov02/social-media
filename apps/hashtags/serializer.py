
from rest_framework import serializers

from apps.hashtags.models import Hashtags

class HashtagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hashtags
        fields = ['id', 'name']
        read_only_fields = ['id']


