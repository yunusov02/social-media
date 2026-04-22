from rest_framework import serializers
from apps.hashtags.models import Hashtags


class HashtagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hashtags
        fields = ['id', 'name', 'created_at']
        read_only_fields = ['id', 'created_at']

    # Normalize BEFORE validation
    def to_internal_value(self, data):
        data = super().to_internal_value(data)

        if 'name' in data:
            name = data['name'].strip().lower()
            name = name.lstrip('#')   # avoid ###django cases
            data['name'] = f'#{name}'

        return data

    def validate_name(self, value):
        qs = Hashtags.all_objects.filter(name=value)

        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)

        if qs.exists():
            raise serializers.ValidationError(
                "A hashtag with this name already exists."
            )

        return value