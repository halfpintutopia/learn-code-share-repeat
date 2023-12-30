import pytest

from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
def test_assessment_model(user, video):
    """
    """
    assessment = Assessment.objects.create(
        user=user,
        video=video,
        understanding=4,
        proficiency=3
    )

    assert assessment.user == user
    assert assessment.unerstanding == 4
    assert assessment.proficiency == 3
