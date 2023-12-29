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

    @staticmethod
    def post(request):
        """
        Create a video
        """
        serializer = VideoSerializer(
            data=request.data,
            context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
