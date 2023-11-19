import io

import pytest
from django.core.exceptions import ValidationError

from app.apps.users.models import Profile
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import get_user_model
from PIL import Image


@pytest.mark.django_db
def test_create_profile():
    """
    GIVEN a profile model
    WHEN creating a profile model
    THEN the user should have successfully create a profile
    """
    User = get_user_model()
    user = User.objects.create_user(
        username="melissasmythe85",
        first_name="Melissa",
        last_name="Smythe",
        email="testuser@testuser.com",
        password="qwerTy123456!"
    )

    image_file = io.BytesIO()
    image = Image.new("RGBA", size=(50, 50), color=(155, 0, 0))
    image.save(image_file, 'png')
    image_file.name = 'test_image.png'
    image_file.seek(0)

    uploaded_image = SimpleUploadedFile(image_file.name, image_file.read(), content_type='image/png')

    background_image_file = io.BytesIO()
    background_image = Image.new("RGBA", size=(50, 50), color=(155, 0, 0))
    background_image.save(background_image_file, 'png')
    background_image_file.name = 'test_background_image.png'
    background_image_file.seek(0)

    uploaded_background_image = SimpleUploadedFile(background_image_file.name, background_image_file.read(),
                                                   content_type='image/png')

    profile = Profile.objects.create(
        user=user,
        location="Switzerland",
        pronoun="she/her",
        website="https://mywebsite.com",
        social={
            "LinkedIn": "https://linkedin/in/mellisasmythe"
        },
        image=uploaded_image,
        background_image=uploaded_background_image
    )

    assert profile.user == user
    assert profile.user.first_name == "Melissa"
    assert profile.user.last_name == "Smythe"
    assert profile.user.email == "testuser@testuser.com"
    assert profile.location == "Switzerland"
    assert profile.pronoun == "she/her"
    assert profile.website == "https://mywebsite.com"
    assert profile.social == {
        "LinkedIn": "https://linkedin/in/mellisasmythe"
    }
    assert 'test_image' in profile.image.name
    assert 'test_background_image' in profile.background_image.name
