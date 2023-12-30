import pytest
from rest_framework import status

from assessment.models import Assessment

from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


@pytest.mark.django_db
def test_get_all_assessments(authenticated_user, assessment):
    """
    GIVEN a request to get all assessments
    WHEN the request is made
    THEN the response should contain all assessments
    """
    request, client, user = authenticated_user
    url = reverse("list-create-assessment")
    res = client.get(url)

    assert res.status_code == 200
    assert len(res.data) == 1


@pytest.mark.django_db
def test_create_assessment(authenticated_user, video):
    """
    GIVEN a request to create an assessment
    WHEN the request is made
    THEN the response should contain the created assessment
    """
    request, client, user = authenticated_user
    url = reverse("list-create-assessment")

    data = {
        "understanding": 4,
        "proficiency": 4,
        "user": user.id,
        "video": video.id,
    }

    res = client.post(url, data=data)

    assert res.status_code == status.HTTP_201_CREATED
    assert res.data["understanding"] == data["understanding"]
    assert res.data["proficiency"] == data["proficiency"]
    assert res.data["user"] == user.id
    assert len(Assessment.objects.all()) == 1


@pytest.mark.django_db
def test_update_assessment(authenticated_user, video):
    """
    GIVEN a request to update an assessment
    WHEN the request is made
    THEN the response should contain the updated assessment
    """
    request, client, user = authenticated_user
    url = reverse("list-create-assessment")

    data = {
        "understanding": 2,
        "proficiency": 2,
        "user": user.id,
        "video": video.id,
    }

    res = client.post(url, data=data)

    assert res.status_code == status.HTTP_201_CREATED
    assert res.data["understanding"] == data["understanding"]
    assert res.data["proficiency"] == data["proficiency"]
    assert res.data["user"] == user.id
    assert len(Assessment.objects.all()) == 1

    url = reverse("get-update-delete-assessment", kwargs={"pk": 1})

    data = {
        "understanding": 3,
        "proficiency": 3,
        "user": user.id,
        "video": video.id,
    }

    res = client.put(url, data=data)

    assert res.status_code == status.HTTP_200_OK
    assert res.data["understanding"] == data["understanding"]
    assert res.data["proficiency"] == data["proficiency"]
    assert res.data["user"] == user.id
    assert len(Assessment.objects.all()) == 1


@pytest.mark.django_db
def test_update_assessment_not_owner(client, user, video, assessment):
    """
    GIVEN a request to update an assessment
    WHEN the request is made by a user who is not the owner
    THEN the response should not update the assessment
    """
    url = reverse("get-update-delete-assessment", kwargs={"pk": 1})

    data = {
        "understanding": 3,
        "proficiency": 3,
        "user": user.id,
        "video": video.id,
    }

    res = client.put(url, data=data)

    assert res.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_delete_assessment(authenticated_user, assessment):
    """
    GIVEN a request to delete an assessment
    WHEN the request is made
    THEN the response should contain the deleted assessment
    """
    request, client, user = authenticated_user
    url = reverse("get-update-delete-assessment", kwargs={"pk": 1})

    res = client.delete(url)

    assert res.status_code == status.HTTP_204_NO_CONTENT
    assert len(Assessment.objects.all()) == 0
