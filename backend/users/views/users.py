from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

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
        profiles = Profile.objects.all()
        serializer = UserProfileSerializer(profiles, many=True)
        return Response(serializer.data)


class GetUpdateUserProfileView(APIView):
    """
    View to get and update user's profile
    """
    permission_classes = [
        IsAuthenticatedOrReadOnly
    ]

    @staticmethod
    def get(request, slug):
        """
        Get the user's profile details
        """
        profile = get_object_or_404(Profile, slug=slug)
        serializer = UserSerializer(profile.user)
        return Response(serializer.data)
