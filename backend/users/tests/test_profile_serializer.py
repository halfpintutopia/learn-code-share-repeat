import io
import pytest

from users.models import Profile
from users.serializers import UserProfileSerializer, UserSerializer, UpdateUserProfileSerializer
from django.test import RequestFactory
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image


@pytest.mark.django_db
def test_profile_serializer(custom_user, uploaded_image, uploaded_background_image):
    """
    GIVEN a valid custom user serializer
    WHEN the data is passed to the serializer
    THEN the serializer should be valid
    """
    profile = Profile.objects.get(user=custom_user)
    profile.location = "Switzerland"
    profile.pronoun = "she/her"
    profile.personal_website = "https://mywebsite.com"
    profile.social_links = {
        "LinkedIn": "https://linkedin/in/mellisasmythe"
    }
    profile.image = uploaded_image
    profile.background_image = uploaded_background_image
    profile.save()

    serializer = UserProfileSerializer(profile)

    assert serializer.data.get('id') == custom_user.id
    assert serializer.data.get("location") == profile.location
    assert serializer.data.get("pronoun") == profile.pronoun
    assert serializer.data.get("personal_website") == profile.personal_website
    assert serializer.data.get("social_links") == profile.social_links
    assert serializer.data.get("image") == profile.image.url
    assert serializer.data.get("background_image") == profile.background_image.url


@pytest.mark.django_db
def test_user_serializer(custom_user):
    """
    GIVEN a valid custom user serializer
    WHEN the data is passed to the serializer
    THEN the serializer should be valid
    """
    serializer = UserSerializer(custom_user)

    assert serializer.data.get("username") == custom_user.username
    assert serializer.data.get("first_name") == custom_user.first_name
    assert serializer.data.get("last_name") == custom_user.last_name
    assert serializer.data.get("email") == custom_user.email


@pytest.mark.django_db
def test_update_user_profile_serializer(custom_user, uploaded_image, uploaded_background_image):
    """
    GIVEN a valid user profile serializer
    WHEN the data is passed to the serializer using a mock request
    THEN the serializer should be valid
    """
    profile = Profile.objects.get(user=custom_user)
    profile.location = "Switzerland"
    profile.pronoun = "she/her"
    profile.personal_website = "https://mywebsite.com"
    profile.social_links = {
        "LinkedIn": "https://linkedin/in/mellisasmythe"
    }
    profile.image = uploaded_image
    profile.background_image = uploaded_background_image
    profile.save()

    data = {
        "personal_website": "https://newwebsite.com",
        "social_links": {
            "LinkedIn": "https://linkedin/user",
            "Facebook": "https://facebook.com/user"
        }
    }
    request = RequestFactory().get("/")
    request.user = custom_user
    serializer = UpdateUserProfileSerializer(profile, data=data, context={"request": request})

    assert serializer.is_valid(raise_exception=True)

    serializer.save()

    updated_profile = Profile.objects.get(user=custom_user)
    updated_user = updated_profile.user

    assert updated_user.username == custom_user.username
    assert updated_user.first_name == custom_user.first_name
    assert updated_user.last_name == custom_user.last_name
    assert updated_user.email == custom_user.email
    assert updated_profile.user_id == custom_user.id
    assert updated_profile.location == profile.location
    assert updated_profile.pronoun == profile.pronoun
    assert updated_profile.personal_website == data["personal_website"]
    assert updated_profile.social_links == data["social_links"]
    assert updated_profile.image == profile.image
    assert updated_profile.background_image == profile.background_image
