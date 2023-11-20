import pytest
from django.contrib.auth import get_user_model
from faker import Faker

# from rest_framework.test import APIClient

User = get_user_model()
fake = Faker()


@pytest.fixture
def custom_user():
    """
    Fixture for creating a user object
    """
    username = fake.username()
    email = fake.email()
    first_name = fake.first_name()
    last_name = fake.last_name()
    password = fake.password()

    return User.objects.create_user(
        username=username,
        email=email,
        fisrt_name=first_name,
        last_name=last_name,
        password=password
    )
