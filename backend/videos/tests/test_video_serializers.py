import pytest

from videos.models import Video
from videos.serializers import VideoSerializer


@pytest.mark.django_db
def test_user_serializer(authenticated_user, uploaded_image, uploaded_video):
    """
    GIVEN a user object
    WHEN a serializer is instantiated with the user object
    THEN the serializer should return a valid representation of the user object
    """
    request, client, user = authenticated_user

    video = Video.objects.create(
        user=user,
        title="Test Video",
        technology_versions="Python 3.9.0",
        image=uploaded_image,
        video=uploaded_video
    )

    serializer = VideoSerializer(
        instance=video,
        context={"request": request}
    )
    data = serializer.data

    assert data["id"] == video.id
    assert data["user"] == user.username
    assert data["title"] == video.title
    assert data["video"] == video.video.url
    assert data["image"] == video.image.url
