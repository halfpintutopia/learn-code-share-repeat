from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from app.permissons import IsOwnerOrReadOnly

from ..serializers import UserProfileSerializer, UserSerializer
from ..models import Profile

User = get_user_model()


# @route
class ListUsers(APIView):
    """
    View to get all users' profiles
    """
    permission_classes = [
        IsAuthenticatedOrReadOnly
    ]

    @staticmethod
    def get(request):
        """
        Get all the users' profile details
        """
        profiles = User.objects.all()
        serializer = UserSerializer(
            profiles,
            many=True,
            context={"request": request}
        )
        return Response(serializer.data)


class GetUpdateUserView(APIView):
    """
    View to get and update user's profile
    """
    permission_classes = [
        IsOwnerOrReadOnly
    ]

    serializer_class = UserSerializer

    def get(self, request, slug):
        """
        Get the user's profile details
        """
        profile = get_object_or_404(Profile, slug=slug)
        user = profile.user
        self.check_object_permissions(self.request, user)

        serializer = UserSerializer(
            user,
            context={"request": request}
        )
        return Response(serializer.data)

    def post(self, request, slug):
        """
        Update the user's profile details
        """

        profile = get_object_or_404(Profile, slug=slug)
        user = profile.user
        self.check_object_permissions(self.request, user)

        serializer = UserSerializer(
            user,
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
