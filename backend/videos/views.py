from django.contrib.auth import get_user_model
from rest_framework import status

from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from app.permissons import IsOwnerOrReadOnly

from .serializers import VideoSerializer
from .models import Video

User = get_user_model()


class VideoList(ListAPIView):
    """
    View to get all videos
    """
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]

    serializer_class = VideoSerializer

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
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class VideoDetail(ListAPIView):
    """
    View to get a single video
    """
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    serializer_class = VideoSerializer

    @staticmethod
    def get(request, pk):
        """
        Get a single video
        """
        video = Video.objects.get(pk=pk)
        serializer = VideoSerializer(
            video,
            context={"request": request}
        )
        return Response(serializer.data)
