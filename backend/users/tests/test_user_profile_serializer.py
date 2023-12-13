import pytest

from django.template.defaultfilters import slugify

from users.models import Profile
from users.serializers import UserProfileSerializer, UserSerializer


@pytest.mark.django_db
def test_user_serializer(user):
    """
    GIVEN a user object
    WHEN a serializer is instantiated with the user object
    THEN the serializer should return a valid representation of the user object
    """
    serializer = UserSerializer(instance=user)
    data = serializer.data

    print(data)

    assert data["id"] == user.id
    assert data["email"] == user.email
    assert data["first_name"] == user.first_name
    assert data["last_name"] == user.last_name
    assert data["username"] == user.username


@pytest.mark.django_db
def test_profile_serializer(user, uploaded_image, uploaded_background_image):
    """
    GIVEN a valid custom user serializer
    WHEN the data is passed to the serializer
    THEN the serializer should be valid
    """
    profile = Profile.objects.get(user=user)
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

    assert serializer.data.get('id') == user.id
    assert serializer.data.get("location") == profile.location
    assert serializer.data.get("pronoun") == profile.pronoun
    assert serializer.data.get("personal_website") == profile.personal_website
    assert serializer.data.get("social_links") == profile.social_links
    assert serializer.data.get("image") == profile.image.url
    assert serializer.data.get("background_image") == profile.background_image.url


@pytest.mark.django_db
def test_user_serializer(user):
    """
    GIVEN a valid custom user serializer
    WHEN the data is passed to the serializer
    THEN the serializer should be valid
    """
    serializer = UserSerializer(user)

    assert serializer.data.get("username") == user.username
    assert serializer.data.get("first_name") == user.first_name
    assert serializer.data.get("last_name") == user.last_name
    assert serializer.data.get("email") == user.email


@pytest.mark.django_db
def test_user_profile_serializer_with_slug(user):
    """
    GIVEN a valid custom user serializer
    WHEN the data is passed to the serializer
    THEN the serializer should be valid and contain a slug
    """
    profile = Profile.objects.get(user=user)

    serializer = UserProfileSerializer(profile)

    assert serializer.data.get('slug') is not None
    assert serializer.data.get("slug") == slugify(user.username)
