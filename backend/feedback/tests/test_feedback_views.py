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


@pytest.mark.django_db
def test_update_feedback(authenticated_user, video, feedback):
    """
    GIVEN a request to update a feedback
    WHEN the request is made
    THEN the response should contain the updated feedback
    """
    request, client, user = authenticated_user
    url = reverse("get-update-delete-feedback", kwargs={"pk": feedback.id})

    data = {
        "video": video.id,
        "clarity": 4,
        "comment": "It has a lot of good terminology, except for one thing"
    }

    res = client.put(url, data=data)

    assert res.status_code == status.HTTP_200_OK
    assert res.data["user"] == user.username
    assert res.data["clarity"] == data["clarity"]
    assert res.data["comment"] == data["comment"]
    assert len(Feedback.objects.all()) == 1


@pytest.mark.django_db
def test_delete_feedback(authenticated_user, feedback):
    """
    GIVEN a request to delete a feedback
    WHEN the request is made
    THEN the response should contain the deleted feedback
    """
    request, client, user = authenticated_user
    url = reverse("get-update-delete-feedback", kwargs={"pk": feedback.id})

    res = client.delete(url)

    assert res.status_code == status.HTTP_204_NO_CONTENT
    assert len(Feedback.objects.all()) == 0
