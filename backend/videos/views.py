from django.contrib.auth import get_user_model
from django.http import Http404

from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView

from app.permissons import IsOwnerOrReadOnly

from .serializers import VideoSerializer
from .models import Video

User = get_user_model()


class VideoList(APIView):
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


class VideoDetail(APIView):
    """
    View to get a single video
    """
    permission_classes = [
        IsOwnerOrReadOnly
    ]

    serializer_class = VideoSerializer

    def get_object(self, pk):
        """
        Helper method to get a single video
        """
        try:
            video = Video.objects.get(pk=pk)
            self.check_object_permissions(self.request, video)
            return video
        except Video.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """
        Retrieve a single video
        """
        video = self.get_object(pk)
        serializer = VideoSerializer(
            video,
            context={"request": request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Update a single video
        """
        video = self.get_object(pk)
        serializer = VideoSerializer(
            video,
            data=request.data,
            context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        """
        Delete a single video
        """
        video = self.get_object(pk)
        video.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
