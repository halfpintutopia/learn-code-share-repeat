from django.contrib.auth import get_user_model

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from app.permissons import IsOwnerOrReadOnly

from .serializers import AssessmentSerializer
from .models import Assessment

User = get_user_model()


class AssessmentList(ListCreateAPIView):
    """
    View to get all the assessments
    Create a new assessment if authenticated
    """
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]

    serializer_class = AssessmentSerializer
    queryset = Assessment.objects.all()

    def perform_create(self, serializer):
        """
        Associate the current logged-in user with the assessment
        """
        serializer.save(user=self.request.user)


class AssessmentDetail(RetrieveUpdateDestroyAPIView):
    """
    View a single assessment
    """
    permission_classes = [
        IsOwnerOrReadOnly
    ]

    serializer_class = AssessmentSerializer
    queryset = Assessment.objects.all()
