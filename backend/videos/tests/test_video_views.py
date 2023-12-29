import pytest

from django.contrib.auth import get_user_model
from django.urls import reverse

from videos.models import Video

User = get_user_model()


@pytest.mark.django_db
def test_get_all_video_view(user, client, uploaded_image, uploaded_video):
    """
    GIVEN a video model
    WHEN a user requests to get all videos
    THEN the user should get a list of all videos
    """
    Video.objects.create(
        user=user,
        image=uploaded_image,
        video=uploaded_video,
        title="Test Video",
        technology_versions="Python 3.9.0"
    )

    url = reverse("list-video")
    res = client.get(url)

    assert res.status_code == 200
    assert res.data[0]["user"] == user.username
    assert len(res.data) == 1
