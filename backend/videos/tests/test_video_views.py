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

    url = reverse("list-create-video")
    res = client.get(url)

    assert res.status_code == 200
    assert res.data[0]["user"] == user.username
    assert len(res.data) == 1


@pytest.mark.django_db
def test_create_video_view(authenticated_user, uploaded_image, uploaded_video):
    """
    GIVEN a video model
    WHEN a user requests to create a video
    THEN the user should get a video created
    """
    request, client, user = authenticated_user

    url = reverse("list-create-video")
    data = {
        "image": uploaded_image,
        "video": uploaded_video,
        "title": "Test Video",
        "technology_versions": "Python 3.9.0"
    }
    res = client.post(url, data=data)

    assert res.status_code == 201
    assert res.data["user"] == user.username
    assert res.data["title"] == "Test Video"


@pytest.mark.django_db
def test_get_single_video_view(user, client, uploaded_image, uploaded_video):
    """
    GIVEN a video model
    WHEN a user requests to get a single video
    THEN the user should get a single video
    """
    video = Video.objects.create(
        user=user,
        image=uploaded_image,
        video=uploaded_video,
        title="Test Video",
        technology_versions="Python 3.9.0"
    )

    url = reverse("get-update-delete-video", kwargs={"pk": video.id})
    res = client.get(url)

    assert res.status_code == 200
    assert res.data["user"] == user.username
    assert res.data["title"] == "Test Video"
