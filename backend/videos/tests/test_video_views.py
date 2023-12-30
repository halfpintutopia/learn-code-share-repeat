import pytest

from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
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


@pytest.mark.django_db
def test_update_video_view(authenticated_user):
    """
    GIVEN a video model
    WHEN a user requests to update a video
    THEN the user should get a video updated
    """
    request, client, user = authenticated_user
    uploaded_image = SimpleUploadedFile(
        name='test_image.jpg',
        content=open('videos/tests/image.jpg', 'rb').read(),
        content_type='image/jpeg'
    )
    uploaded_video = SimpleUploadedFile(
        name='test_video.mp4',
        content=open('videos/tests/test_video.mp4', 'rb').read(),
        content_type='video/mp4'
    )
    video = Video.objects.create(
        user=user,
        image=uploaded_image,
        video=uploaded_video,
        title="Test Video",
        technology_versions="Python 3.9.0"
    )

    different_uploaded_image = SimpleUploadedFile(
        name='different_test_image.jpg',
        content=open('videos/tests/image.jpg', 'rb').read(),
        content_type='image/jpeg'
    )
    different_uploaded_video = SimpleUploadedFile(
        name='different_test_video.mp4',
        content=open('videos/tests/video.mp4', 'rb').read(),
        content_type='video/mp4'
    )

    url = reverse(
        "get-update-delete-video",
        kwargs={"pk": video.id}
    )
    data = {
        "image": different_uploaded_image,
        "video": different_uploaded_video,
        "title": "Another Test Video",
        "technology_versions": "Python 3.8.0"
    }
    res = client.put(
        url,
        data=data,
        format='multipart'
    )

    assert res.status_code == 200
    assert res.data["user"] == user.username
    assert res.data["title"] == "Another Test Video"


@pytest.mark.django_db
def test_delete_video_view(authenticated_user, uploaded_image, uploaded_video):
    """
    GIVEN a video model
    WHEN a user requests to delete a video
    THEN the user should get a video deleted
    """
    request, client, user = authenticated_user
    video = Video.objects.create(
        user=user,
        image=uploaded_image,
        video=uploaded_video,
        title="Test Video",
        technology_versions="Python 3.9.0"
    )

    url = reverse("get-update-delete-video", kwargs={"pk": video.id})
    res = client.delete(url)

    assert res.status_code == 204
    assert res.data is None


@pytest.mark.django_db
def test_update_video_view_with_non_authenticated_user(client, user):
    """
    GIVEN a video model
    WHEN a user requests to update a video
    THEN the user should get a video updated
    """
    uploaded_image = SimpleUploadedFile(
        name='test_image.jpg',
        content=open('videos/tests/image.jpg', 'rb').read(),
        content_type='image/jpeg'
    )
    uploaded_video = SimpleUploadedFile(
        name='test_video.mp4',
        content=open('videos/tests/test_video.mp4', 'rb').read(),
        content_type='video/mp4'
    )
    video = Video.objects.create(
        user=user,
        image=uploaded_image,
        video=uploaded_video,
        title="Test Video",
        technology_versions="Python 3.9.0"
    )

    different_uploaded_image = SimpleUploadedFile(
        name='different_test_image.jpg',
        content=open('videos/tests/image.jpg', 'rb').read(),
        content_type='image/jpeg'
    )
    different_uploaded_video = SimpleUploadedFile(
        name='different_test_video.mp4',
        content=open('videos/tests/video.mp4', 'rb').read(),
        content_type='video/mp4'
    )

    url = reverse(
        "get-update-delete-video",
        kwargs={"pk": video.id}
    )
    data = {
        "image": different_uploaded_image,
        "video": different_uploaded_video,
        "title": "Another Test Video",
        "technology_versions": "Python 3.8.0"
    }
    res = client.put(
        url,
        data=data,
        format='multipart'
    )

    assert res.status_code == 401


@pytest.mark.django_db
def test_retrieve_video_with_invalid_id(client, user):
    """
    GIVEN a video model
    WHEN a user requests to get a video with an invalid id
    THEN the user should get a 404 error
    """
    url = reverse(
        "get-update-delete-video",
        kwargs={"pk": 1}
    )
    res = client.get(url)

    assert res.status_code == 404
