from django.contrib.auth import get_user_model
from django.db.models import Count, Max
from rest_framework import filters

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from app.permissons import IsOwnerOrReadOnly

from .serializers import VideoSerializer
from .models import Video

User = get_user_model()


class VideoList(ListCreateAPIView):
    """
    View to get all videos
    """
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    # queryset = Video.objects.all()
    queryset = Video.objects.annotate(
        feedback_count=Count('feedback', distinct=True),
        latest_feedback_created_at=Max('feedback__created_at')
    ).order_by('-latest_feedback_created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    search_fields = [
        'title',
        'user__username',
    ]
    ordering_fields = [
        'feedback_count',
        'latest_feedback_created_at',
    ]
    serializer_class = VideoSerializer


class VideoDetail(RetrieveUpdateDestroyAPIView):
    """
    View to get a single video
    """
    permission_classes = [
        IsOwnerOrReadOnly
    ]
    # queryset = Video.objects.all()
    queryset = Video.objects.annotate(
        feedback_count=Count('feedback', distinct=True),
        latest_feedback_created_at=Max('feedback__created_at')
    ).order_by('-latest_feedback_created_at')

    serializer_class = VideoSerializer
