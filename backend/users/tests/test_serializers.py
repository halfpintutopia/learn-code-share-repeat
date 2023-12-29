import pytest

from django.template.defaultfilters import slugify

from users.models import Profile
from users.serializers import UserProfileSerializer, UserSerializer


@pytest.mark.django_db
def test_user_serializer(authenticated_user):
    """
    GIVEN a user object
    WHEN a serializer is instantiated with the user object
    THEN the serializer should return a valid representation of the user object
    """
    request, client, user = authenticated_user

    serializer = UserSerializer(
        instance=user,
        context={"request": request}
    )
    data = serializer.data

    assert data["id"] == user.id
    assert data["email"] == user.email
    assert data["first_name"] == user.first_name
    assert data["last_name"] == user.last_name
    assert data["username"] == user.username


@pytest.mark.django_db
def test_profile_serializer(
        authenticated_user,
        uploaded_image,
        uploaded_background_image
):
    """
    GIVEN a valid custom user serializer
    WHEN the data is passed to the serializer
    THEN the serializer should be valid
    """
    request, client, user = authenticated_user

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

    serializer = UserProfileSerializer(
        profile,
        context={"request": request}
    )

    assert serializer.data.get('id') == user.id
    assert serializer.data.get("location") == profile.location
    assert serializer.data.get("pronoun") == profile.pronoun
    assert serializer.data.get("personal_website") == profile.personal_website
    assert serializer.data.get("social_links") == profile.social_links
    assert serializer.data.get("image") == profile.image.url
    assert serializer.data.get("background_image") == profile.background_image.url


@pytest.mark.django_db
def test_user_profile_serializer_with_slug(authenticated_user):
    """
    GIVEN a valid custom user serializer
    WHEN the data is passed to the serializer
    THEN the serializer should be valid and contain a slug
    """
    request, client, user = authenticated_user

    profile = Profile.objects.get(user=user)

    serializer = UserProfileSerializer(
        profile,
        context={"request": request}
    )

    assert serializer.data.get('slug') is not None
    assert serializer.data.get("slug") == slugify(user.username)


@pytest.mark.django_db
def test_contains_expected_fields(authenticated_user):
    """
    GIVEN a valid custom user serializer
    WHEN the data is passed to the serializer
    THEN the serializer should be valid and contain the expected fields
    """
    request, client, user = authenticated_user

    profile = Profile.objects.get(user=user)

    serializer = UserProfileSerializer(
        profile,
        context={"request": request}
    )

    data = serializer.data

    assert set(data.keys()) == {"id", "user", "slug", "location", "pronoun", "personal_website", "social_links",
                                "image", "background_image", "joined_date", "is_email_verified",
                                "email_verification_token", "is_owner"}
