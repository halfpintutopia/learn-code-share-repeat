import pytest

from feedback.models import Feedback
from django.contrib.auth import get_user_model

from videos.models import Video

User = get_user_model()


@pytest.mark.django_db
def test_feedback_model(user, uploaded_image, uploaded_video):
    """
    GIVEN a feedback model
    WHEN creating a feedback model
    THEN the user should have successfully created a feedback
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

    clarity = 5
    comment = "This is a comment"
    feedback = Feedback.objects.create(
        user=user,
        video=video,
        clarity=clarity,
        comment=comment
    )

    assert feedback.user == user
    assert feedback.clarity == clarity
    assert feedback.comment == comment
    assert len(Feedback.objects.all()) == 1
