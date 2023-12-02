from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Profile

User = get_user_model()


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
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

    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'username',
        ]
        read_only_fields = ['id', 'email']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
