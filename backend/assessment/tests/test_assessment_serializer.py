import pytest

from assessment.models import Assessment
from assessment.serializers import AssessmentSerializer

from django.contrib.auth import get_user_model

from videos.models import Video

User = get_user_model()


@pytest.mark.django_db
def test_assessment_serializer(authenticated_user, uploaded_image, uploaded_video):
    """
    GIVEN an assessment object
    WHEN a serializer is instantiated with the assessment object
    THEN the serializer should return a valid representation of the assessment object
    """
    request, client, user = authenticated_user

    technology_versions = "React 18"
    title = "Creating a simple component"
    video = Video.objects.create(
        user=user,
        image=uploaded_image,
        video=uploaded_video,
        title=title,
        technology_versions=technology_versions
    )

    assessment = Assessment.objects.create(
        user=user,
        video=video,
        understanding=5,
        proficiency=5
    )

    serializer = AssessmentSerializer(
        instance=assessment,
        context={"request": request}
    )

    data = serializer.data

    assert data["id"] == assessment.id
    assert data["user"] == user.id
    assert data["understanding"] == assessment.understanding
    assert data["proficiency"] == assessment.proficiency
