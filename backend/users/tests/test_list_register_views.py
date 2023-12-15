import pytest

from django.contrib.auth import get_user_model
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient, force_authenticate

from faker import Faker

User = get_user_model()
fake = Faker()


@pytest.mark.django_db
def test_list_users(client, user):
    """
    GIVEN 1 user instance in the database
    WHEN a GET request is made to the list-users endpoint
    THEN there should be 1 user returned
    """
    url = reverse('list-users')
    res = client.get(url)

    assert res.status_code == status.HTTP_200_OK
    assert len(res.data) == 1


@pytest.mark.django_db
def test_create_user(client):
    """
    GIVEN a valid user object
    WHEN a POST request is made to the user-create endpoint
    THEN a new user is created
    """
    users = User.objects.all()
    assert len(users) == 0
    password = fake.password()

    user = {
        "username": fake.first_name(),
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "password": password
    }

    url = reverse('register-user')

    res = client.post(url, user, content_type="application/json")

    assert res.status_code == status.HTTP_201_CREATED
    assert res.data["username"] == user["username"]
    assert res.data["first_name"] == user["first_name"]
    assert res.data["last_name"] == user["last_name"]
    assert res.data["email"] == user["email"]

    created_user = User.objects.get(username=user["username"])
    assert created_user.user_profile is not None
    assert created_user.user_profile.email_verification_token is not None


@pytest.mark.django_db
def test_activate_user(client, user):
    """
    GIVEN a valid user object
    WHEN a GET request is made to the activate endpoint
    THEN the user's is_email_verified field should be True
    """
    uidb64 = urlsafe_base64_encode(force_bytes(user.pk))

    url = reverse("activate", kwargs={
        "uidb64": uidb64,
        "token": user.user_profile.email_verification_token
    })
    res = client.get(url)

    assert res.status_code == status.HTTP_200_OK
    assert res.data["message"] == "Thank you for confirming your email . Now you can login to you account"
