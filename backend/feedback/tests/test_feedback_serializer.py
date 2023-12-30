import pytest

from feedback.models import Feedback
from django.contrib.auth import get_user_model

from feedback.serializers import FeedbackSerializer
from videos.models import Video

User = get_user_model()


@pytest.mark.django_db
def test_feedback_serializer(authenticated_user, uploaded_image, uploaded_video):
    """
    GIVEN a feedback object
    WHEN a serializer is instantiated with the feedback object
    THEN the serializer should return a valid representation of the feedback object
    """
    request, client, user = authenticated_user

    technology_versions = "React 18"
    title = "Creating a simple component"
    video = Video.objects.create(
        user=user,
        image=uploaded_image,
        video=uploaded_video,
        title=title,
        technology_versions=technology_versions
    )

    feedback = Feedback.objects.create(
        user=user,
        video=video,
        clarity=5,
        comment="This is a comment"
    )

    serializer = FeedbackSerializer(
        instance=feedback,
        context={"request": request}
    )

    data = serializer.data

    assert data["id"] == feedback.id
    assert data["user"] == user.username
    assert data["clarity"] == feedback.clarity
    assert data["comment"] == feedback.comment
    assert len(Feedback.objects.all()) == 1
