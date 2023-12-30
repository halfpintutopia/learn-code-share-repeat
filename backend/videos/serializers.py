from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Video

User = get_user_model()


class VideoSerializer(serializers.ModelSerializer):
    """
    Serializer for the Video model.
    'user' field represents the associated username
    """
    user = serializers.ReadOnlyField(source='user.username')
    is_owner = serializers.SerializerMethodField()
    profile_user_id = serializers.ReadOnlyField(source='user.id')
    profile_image = serializers.ReadOnlyField(source='user.profile.image.url')

    def get_is_owner(self, obj):
        """
        Check if the current user is the owner of the video
        """
        request = self.context["request"]

        if request and not request.user.is_anonymous:
            return request.user == obj.user
        return False

    def update(self, instance, validated_data):
        """
        Update the video instance
        """
        instance.title = validated_data.get('title', instance.title)
        instance.technology_versions = validated_data.get('technology_versions', instance.technology_versions)
        instance.video = validated_data.get('video', instance.video)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance

    class Meta:
        """
        Fields to include in the serializer and read-only fields
        """
        model = Video
        fields = [
            "id",
            "user",
            "profile_user_id",
            "profile_image",
            "title",
            "technology_versions",
            "video",
            "image",
            "created_at",
            "updated_at",
            "is_owner"
        ]
        read_only_fields = [
            'id',
            "created_at",
            "updated_at"
        ]
