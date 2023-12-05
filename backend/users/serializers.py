from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from django.utils.translation import gettext_lazy as _
from django.template.loader import render_to_string
from rest_framework import serializers

from .models import Profile

User = get_user_model()


class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the UserProfile model. 'user' field represents the associated username
    'id' and 'joined_date' fields are read-only
    """
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        """
        Fields to include in the serializer and read-only fields
        """
        model = Profile
        fields = [
            "id",
            "user",
            "location",
            "pronoun",
            "personal_website",
            "social_links",
            "image",
            "background_image",
            "joined_date"
        ]
        read_only_fields = ['id', "joined_date"]


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model. 'user_profile' field represents the associated profile
    'id' and 'email' fields are read-only
    """

    user_profile = UserProfileSerializer(read_only=True)

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
        ]
        read_only_fields = ['id', 'email']

    def create(self, validated_data):
        """
        Create a new user and profile instance. Send an email notification to the user
        """
        user = User.objects.create_user(**validated_data)
        return user
