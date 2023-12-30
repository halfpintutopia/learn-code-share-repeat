import pytest

from django.contrib.auth import get_user_model

from assessment.models import Assessment

User = get_user_model()


@pytest.mark.django_db
def test_assessment_model(user, video):
    """
    GIVEN an assessment model
    WHEN creating an assessment model
    THEN the user should have successfully created an assessment
    """
    assessment = Assessment.objects.create(
        user=user,
        video=video,
        understanding=4,
        proficiency=3
    )

    assert assessment.user == user
    assert assessment.understanding == 4
    assert assessment.proficiency == 3
