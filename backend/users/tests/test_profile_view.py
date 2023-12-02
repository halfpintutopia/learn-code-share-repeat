import pytest

from django.contrib.auth import get_user_model
from faker import Faker
from django.urls import reverse
from rest_framework import status

User = get_user_model()
fake = Faker()


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

    url = reverse('user-create-list')

    res = client.post(url, user, content_type="application/json")

    assert res.status_code == status.HTTP_201_CREATED
    assert res.data["username"] == user["username"]
    assert res.data["first_name"] == user["first_name"]
    assert res.data["last_name"] == user["last_name"]
    assert res.data["email"] == user["email"]

    created_user = User.objects.get(username=user["username"])
    assert created_user.check_password(password)
    assert created_user.user_profile is not None
