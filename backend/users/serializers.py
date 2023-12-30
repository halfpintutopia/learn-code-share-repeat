from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Profile

User = get_user_model()


class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the UserProfile model. 'user' field represents the associated username
    'id' and 'joined_date' fields are read-only
    """
    user = serializers.ReadOnlyField(source='user.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """
        Check if the current user is the owner of the profile
        """
        request = self.context["request"]

        if request and not request.user.is_anonymous:
            return request.user == obj.user
        return False

    class Meta:
        """
        Fields to include in the serializer and read-only fields
        """
        model = Profile
        fields = [
            "id",
            "user",
            "slug",
            "location",
            "pronoun",
            "personal_website",
            "social_links",
            "image",
            "background_image",
            "joined_date",
            "is_email_verified",
            "email_verification_token",
            "is_owner"
        ]
        read_only_fields = [
            'id',
            'slug',
            "joined_date",
            "is_email_verified",
            "email_verification_token"
        ]


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model. 'user_profile' field represents the associated profile
    'id' and 'email' fields are read-only
    """

    user_profile = UserProfileSerializer(read_only=True)
    videos_count = serializers.ReadOnlyField()

    class Meta:
        """
        Fields to include in the serializer and read-only fields
        """
        model = User
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'username',
            'user_profile',
            "videos_count",
        ]
        read_only_fields = ['id']

    def create(self, validated_data):
        """
        Create a new user and profile instance
        """
        user = User.objects.create_user(**validated_data)
        return user
