import io

import pytest

from users.models import Profile
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import get_user_model
from PIL import Image

User = get_user_model()


@pytest.mark.django_db
def test_profile_model(custom_user, uploaded_image, uploaded_background_image):
    """
    GIVEN a profile model
    WHEN creating a profile model
    THEN the user should have successfully created a profile
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

    assert profile.user == custom_user
    assert profile.user.first_name == custom_user.first_name
    assert profile.user.last_name == custom_user.last_name
    assert profile.user.email == custom_user.email
    assert profile.location == "Switzerland"
    assert profile.pronoun == "she/her"
    assert profile.personal_website == "https://mywebsite.com"
    assert profile.social_links == {
        "LinkedIn": "https://linkedin/in/mellisasmythe"
    }
    assert 'test_image' in profile.image.name
    assert 'test_background_image' in profile.background_image.name
