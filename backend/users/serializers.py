from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from rest_framework import serializers

from django.utils.translation import gettext_lazy as _

from .models import Profile

User = get_user_model()


class UserProfileSerializer(serializers.ModelSerializer):
    """
     Serializer that converts the user's profile into JSON
    """
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        """
        Specify the model and fields to serialize
        """
        model = Profile
        fields = [
            "id",
            "owner",
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
    Serializer that converts the user model to JSON
    """
    user_profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ["id", "email", "first_name", "last_name", "username", "user_profile"]
        read_only_fields = ["id", "email"]
        extra_kwargs = {'password': {'write_only': True}}

    # def create(self, validated_data):
    #     """
    #     Helper function that creates the user's profile
    #     and sends an email to the user
    #     """
    #     profile_data = validated_data.pop("user_profile")
    #
    #     user = User.objects.create(
    #         username=validated_data.get("username"),
    #         first_name=validated_data.get("first_name"),
    #         last_name=validated_data.get("last_name"),
    #         email=validated_data.get("email"),
    #     )
    #
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     Profile.objects(user=user, **profile_data)
    #     self.send_notification_email(email=user.email)
    #     return user

# class UpdateUserProfileSerializer(serializers.Serializer):
#     """
#     Serializer that converts the user's profile into JSON
#     and updates the user's profile
#     then sends an email to the user
#     """
#     username = serializers.CharField(
#         label=_("Username"),
#         write_only=True,
#         required=False,
#         allow_blank=True
#     )
#     first_name = serializers.CharField(
#         label=_("First Name"),
#         write_only=True,
#         required=False,
#         allow_blank=True
#     )
#     last_name = serializers.CharField(
#         label=_("Last Name"),
#         write_only=True,
#         required=False,
#         allow_blank=True
#     )
#     pronoun = serializers.CharField(
#         label=_("Pronoun"),
#         write_only=True,
#         required=False,
#         allow_blank=True
#     )
#     personal_website = serializers.URLField(
#         label=_("Website"),
#         write_only=True,
#         required=False,
#         allow_blank=True
#     )
#     social_links = serializers.JSONField(
#         label=_("Social"),
#         write_only=True,
#         required=False
#     )
#     image = serializers.ImageField(
#         label=_("Profile Image"),
#         write_only=True,
#         required=False
#     )
#     background_image = serializers.ImageField(
#         label=_("Background Image"),
#         write_only=True,
#         required=False
#     )
#     joined_date = serializers.DateTimeField(
#         label=_("Joined Date"),
#         write_only=True,
#         required=False
#     )
#
#     @staticmethod
#     def validate_username(username):
#         """
#         Helper function that validates the username
#         """
#         if not username:
#             raise serializers.ValidationError({
#                 "username": "Please enter a username."
#             })
#         else:
#             return username
#
#     @staticmethod
#     def validate_first_name(first_name):
#         """
#         Helper function that validates the first name
#         """
#         if not first_name:
#             raise serializers.ValidationError({
#                 "first_name": _("Please enter your first name.")
#             })
#         else:
#             return first_name
#
#     @staticmethod
#     def validate_last_name(last_name):
#         """
#         Helper function that validates the last name
#         """
#         if not last_name:
#             raise serializers.ValidationError({
#                 "last_name": _("Please enter your last name,")
#             })
#         else:
#             return last_name
#
#     @staticmethod
#     def validate_location(location):
#         """
#         Helper function that validates the location
#         """
#         if not location:
#             raise serializers.ValidationError({
#                 "location": _("Please enter your location.")
#             })
#         else:
#             return location
#
#     @staticmethod
#     def validate_email(email):
#         """
#         Helper function that validates the email
#         """
#         if User.objects.filter(email=email).exists():
#             raise serializers.ValidationError({
#                 "email": _("A user with this email already exists.")
#             })
#         return email
#
#     @staticmethod
#     def send_notification_email(email):
#         """
#         Helper function that sends an email to the user
#         """
#         message = EmailMessage(
#             subject=_("Updated user profile creation"),
#             body=_("Updated user profile creation"),
#             to=[email],
#         )
#         message.send()
#
#     # def create(self, validated_data):
#     #     """
#     #
#     #     """
#     #     user = User.objects.create_user(**validated_data)
#     #     return user
#
#     def update(self, instance, validated_data):
#         """
#         Helper function that updates the user's profile
#         and sends an email to the user
#         """
#         user_data = validated_data.pop("user", {})
#         user = instance.user
#
#         for attr, value in user_data.items():
#             setattr(user, attr, value)
#         instance.save()
#         for attr, value in validated_data.items():
#             setattr(instance, attr, value)
#         instance.save()
#
#         self.send_notification_email(email=user.email)
#
#         return instance
