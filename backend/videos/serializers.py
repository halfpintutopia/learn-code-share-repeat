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

    def create(self, validated_data):
        """
        Create a video
        """
        user = self.context["request"].user
        return Video.objects.create(user=user, **validated_data)
