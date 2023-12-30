import io

import pytest

from mixer.backend.django import mixer

from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile

from rest_framework.test import APIClient, APIRequestFactory

from faker import Faker

from PIL import Image

from assessment.models import Assessment
from feedback.models import Feedback
from videos.models import Video

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
def uploaded_video():
    """
    Fixture for creating a video file
    """
    with open("videos/tests/test_video.mp4", "rb") as video:
        return SimpleUploadedFile("test_video.mp4", video.read(), content_type="video/mp4")


@pytest.fixture(scope="function")
def video(user, uploaded_image, uploaded_video):
    """
    Fixture for creating a video object
    """
    technology_versions = "React 18"
    title = "Creating a simple component"
    return mixer.blend(
        Video,
        user=user,
        image=uploaded_image,
        video=uploaded_video,
        title=title,
        technology_versions=technology_versions
    )


@pytest.fixture(scope="function")
def feedback(user, video):
    """
    Fixture for creating a feedback object
    """
    return mixer.blend(
        Feedback,
        user=user,
        video=video,
        clarity=5,
        comment="This is a comment"
    )


@pytest.fixture(scope="function")
def assessment(user, video):
    """
    Fixture for creating an assessment object
    """
    return mixer.blend(
        Assessment,
        user=user,
        video=video,
        understanding=4,
        proficiency=4
    )
