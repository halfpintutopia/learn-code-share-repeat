import pytest

from feedback.models import Feedback
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
def test_feedback_model(video):
    """
    GIVEN a feedback model
    WHEN creating a feedback model
    THEN the user should have successfully created a feedback
    """
    video, user = video
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
