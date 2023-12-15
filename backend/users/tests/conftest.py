import io

import pytest

from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile

from rest_framework.test import APIClient, APIRequestFactory

from faker import Faker

from PIL import Image

User = get_user_model()
fake = Faker()


@pytest.fixture(scope="function")
def user():
    """
    Fixture for creating a user object
    """
    username = fake.first_name()
    email = fake.email()
    first_name = fake.first_name()
    last_name = fake.last_name()
    password = fake.password()

    return User.objects.create_user(
        username=username,
        email=email,
        first_name=first_name,
        last_name=last_name,
        password=password
    )


@pytest.fixture(scope="function")
def authenticated_user(user):
    """
    Fixture for creating an authenticated user object
    """
    factory = APIRequestFactory()
    request = factory.get("/")
    request.user = user

    client = APIClient()
    client.force_authenticate(user=user)

    return request, client, user


@pytest.fixture(scope="function")
def uploaded_image():
    """
    Fixture for creating an image file
    """
    image_file = io.BytesIO()
    image = Image.new("RGBA", size=(50, 50), color=(155, 0, 0))
    image.save(image_file, 'png')
    image_file.name = 'test_image.png'
    image_file.seek(0)

    uploaded_image = SimpleUploadedFile(image_file.name, image_file.read(), content_type='image/png')

    return uploaded_image


@pytest.fixture(scope="function")
def uploaded_background_image():
    """
    Fixture for creating a background image file
    """
    background_image_file = io.BytesIO()
    background_image = Image.new("RGBA", size=(50, 50), color=(155, 0, 0))
    background_image.save(background_image_file, 'png')
    background_image_file.name = 'test_background_image.png'
    background_image_file.seek(0)

    uploaded_background_image = SimpleUploadedFile(background_image_file.name, background_image_file.read(),
                                                   content_type='image/png')

    return uploaded_background_image
