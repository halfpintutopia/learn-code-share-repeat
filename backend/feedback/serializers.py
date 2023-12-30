from django.contrib.auth import get_user_model
from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers

from .models import Feedback

User = get_user_model()


class FeedbackSerializer(serializers.ModelSerializer):
    """
    Serializer for the Feedback model.
    'user' field represents the associated username
    """
    user = serializers.ReadOnlyField(source='user.username')
    is_owner = serializers.SerializerMethodField()
    profile_user_id = serializers.ReadOnlyField(source='user.id')
    profile_image = serializers.ReadOnlyField(source='user.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """
        Check if the current user is the owner of the video
        """
        request = self.context["request"]

        if request and not request.user.is_anonymous:
            return request.user == obj.user
        return False

    def get_created_at(self, obj):
        """
        Get the created_at field
        """
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        """
        Get the updated_at field
        """
        return naturaltime(obj.updated_at)

    class Meta:
        """
        Fields to include in the serializer and read-only fields
        """
        model = Feedback
        fields = [
            "id",
            "user",
            "is_owner",
            "profile_user_id",
            "profile_image",
            "clarity",
            "comment",
            "created_at",
            "updated_at"
        ]
        read_only_fields = [
            'id',
            "created_at",
            "updated_at"
        ]


class FeedbackDetailSerializer(FeedbackSerializer):
    """
    Serializer for the Feedback model used in the detail view.
    Video is a read-only field so that we don't have to pass the video id in the request body
    """
    video = serializers.ReadOnlyField(source='video.id')
