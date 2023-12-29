import pytest

import requests

from django.contrib.auth import get_user_model
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
        "slug": user.user_profile.slug,
    })

    res = client.get(url)

    assert res.status_code == status.HTTP_200_OK
    assert res.data.get("id") == user.id
    assert res.data.get("username") == user.username
    assert res.data.get("first_name") == user.first_name
    assert res.data.get("last_name") == user.last_name
    assert res.data.get("user_profile") is not None


@pytest.mark.django_db
def test_auth_token(client):
    """
    GIVEN a user instance in the database
    WHEN a POST request is made to the token endpoint with valid credentials
    THEN a token pair should be generated
    """
    username = fake.first_name()
    email = fake.email()
    password = fake.password()

    User.objects.create_user(
        username=username,
        email=email,
        password=password
    )

    data = {
        'username': username,
        'password': password
    }
    url = reverse("token_obtain_pair")
    res = client.post(
        url, data
    )

    assert res.status_code == status.HTTP_200_OK
    assert res.data.get("refresh") is not None
    assert res.data.get("access") is not None
