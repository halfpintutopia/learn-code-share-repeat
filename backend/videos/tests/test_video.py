import pytest

from django.contrib.auth import get_user_model

from videos.models import Video

User = get_user_model()


@pytest.mark.django_db
def test_video_model(user, uploaded_image, uploaded_video):
    """
    GIVEN a video model
    WHEN creating a video model
    THEN the user should have successfully created a video entry
    """
    technology_versions = "React 18"
    title = "Creating a simple component"
    video = Video.objects.create(
        user=user,
        image=uploaded_image,
        video=uploaded_video,
        title=title,
        technology_versions=technology_versions
    )

    assert video.user == user
    assert video.technology_versions == technology_versions

    uploaded_image.seek(0)
    assert video.image.read() == uploaded_image.read()
    uploaded_video.seek(0)
    assert video.video.read() == uploaded_video.read()
