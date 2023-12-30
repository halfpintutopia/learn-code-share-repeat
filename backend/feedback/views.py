from django.contrib.auth import get_user_model
from django.http import Http404

from mixer.backend.django import mixer

from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView

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

    # def get_object(self, pk):
    #     """
    #     Helper method to get a single feedback
    #     """
    #     try:
    #         feedback = Feedback.objects.get(pk=pk)
    #         self.check_object_permissions(self.request, feedback)
    #         return feedback
    #     except Feedback.DoesNotExist:
    #         raise Http404
    #
    # def get(self, request, pk):
    #     """
    #     Retrieve a single feedback
    #     """
    #     feedback = self.get_object(pk)
    #     serializer = FeedbackDetailSerializer(
    #         feedback,
    #         context={"request": request}
    #     )
    #     return Response(serializer.data)
    #
    # def put(self, request, pk):
    #     """
    #     Update a single feedback
    #     """
    #     feedback = self.get_object(pk)
    #     serializer = FeedbackDetailSerializer(
    #         feedback,
    #         data=request.data,
    #         context={"request": request}
    #     )
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(
    #         serializer.errors,
    #         status=status.HTTP_400_BAD_REQUEST
    #     )
    #
    # def delete(self, request, pk):
    #     """
    #     Delete a single feedback
    #     """
    #     feedback = self.get_object(pk)
    #     feedback.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
