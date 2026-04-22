from rest_framework import serializers
from .models import Post
from apps.hashtags.models import Hashtags
from apps.hashtags.serializer import HashtagSerializer

class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    hashtags = HashtagSerializer(many=True, read_only=True)
    # This allows sending ["python", "django"] in the request
    hashtag_names = serializers.ListField(
        child=serializers.CharField(),
        write_only=True,
        required=False
    )

    class Meta:
        model = Post
        fields = [
            'id', 'user', 'title', 'content', 
            'hashtags', 'hashtag_names', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']

    def create(self, validated_data):
        hashtag_names = validated_data.pop('hashtag_names', [])
        post = Post.objects.create(**validated_data)
        
        for name in hashtag_names:
            # Normalize name (e.g. "Django" -> "#django")
            clean_name = f"#{name.strip().lower().lstrip('#')}"
            hashtag, _ = Hashtags.objects.get_or_create(name=clean_name)
            post.hashtags.add(hashtag)
            
        return post

    def update(self, instance, validated_data):
        # Update logic for hashtags can be added here if needed
        return super().update(instance, validated_data)