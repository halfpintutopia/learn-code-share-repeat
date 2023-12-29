from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import status

from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from app.permissons import IsOwnerOrReadOnly

from .serializers import VideoSerializer
from .models import Video

User = get_user_model()


class VideoList(ListAPIView):
    """
    View to get all videos
    """
    permission_classes = [
        IsOwnerOrReadOnly
    ]

    @staticmethod
    def get(request):
        """
        Get all the videos
        """
        videos = Video.objects.all()
        serializer = VideoSerializer(
            videos,
            many=True,
            context={"request": request}
        )
        return Response(serializer.data)
