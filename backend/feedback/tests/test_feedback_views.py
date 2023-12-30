import pytest
from rest_framework import status

from feedback.models import Feedback
from django.contrib.auth import get_user_model
from django.urls import reverse

from feedback.serializers import FeedbackSerializer
from videos.models import Video

User = get_user_model()


@pytest.mark.django_db
def test_get_all_feedback(authenticated_user, feedback):
    """
    GIVEN a request to get all feedbacks
    WHEN the request is made
    THEN the response should contain all feedbacks
    """
    request, client, user = authenticated_user
    url = reverse("list-create-feedback")
    res = client.get(url)

    assert res.status_code == status.HTTP_200_OK
    assert len(res.data) == 1


@pytest.mark.django_db
def test_create_feedback(authenticated_user, video):
    """
    GIVEN a request to create a feedback
    WHEN the request is made
    THEN the response should contain the created feedback
    """
    request, client, user = authenticated_user
    url = reverse("list-create-feedback")

    data = {
        "video": video.id,
        "clarity": 5,
        "comment": "This is a comment"
    }

    res = client.post(url, data=data)

    assert res.status_code == status.HTTP_201_CREATED
    assert res.data["user"] == user.username
    assert res.data["clarity"] == data["clarity"]
    assert res.data["comment"] == data["comment"]
    assert len(Feedback.objects.all()) == 1
