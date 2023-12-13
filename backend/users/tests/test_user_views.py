import pytest

from django.contrib.auth import get_user_model
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from faker import Faker
from django.urls import reverse
from rest_framework import status

User = get_user_model()
fake = Faker()


@pytest.mark.django_db
def test_user_login(client, user):
    """
    GIVEN a user instance in the database
    WHEN a POST request is made to the login endpoint with valid credentials
    THEN the user should be logged in
    """
    client.login(
        username=user.username,
        password=user.password
    )

    url = reverse("retrieve-edit-user", kwargs={
        "userId": user.id,
    })

    res = client.get(url)

    assert res.status_code == status.HTTP_200_OK
    assert res.data['username'] == user.username
