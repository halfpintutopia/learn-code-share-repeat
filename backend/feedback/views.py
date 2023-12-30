from django.contrib.auth import get_user_model

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from app.permissons import IsOwnerOrReadOnly

from .serializers import FeedbackSerializer, FeedbackDetailSerializer
from .models import Feedback

User = get_user_model()


class FeedbackList(ListCreateAPIView):
    """
    View to get all the feedbacks
    Create a new feedback if authenticated
    """
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]

    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()

    def perform_create(self, serializer):
        """
        Associate the current logged-in user with the feedback
        """
        serializer.save(user=self.request.user)


class FeedbackDetail(RetrieveUpdateDestroyAPIView):
    """
    View a single feedback
    """
    permission_classes = [
        IsOwnerOrReadOnly
    ]

    serializer_class = FeedbackDetailSerializer
    queryset = Feedback.objects.all()
