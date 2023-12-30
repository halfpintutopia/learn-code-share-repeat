from django.contrib.auth import get_user_model
from django.http import Http404
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from app.permissons import IsOwnerOrReadOnly

from ..serializers import UserSerializer
from ..models import Profile

User = get_user_model()


# @route
class ListUsers(ListAPIView):
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

    def get_object(self, slug):
        """
        Helper method to get the user's profile
        """
        try:
            profile = Profile.objects.get(slug=slug)
            self.check_object_permissions(self.request, profile)
            return profile
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, slug):
        """
        Get the user's profile details
        """
        profile = self.get_object(slug)
        user = profile.user
        self.check_object_permissions(self.request, user)

        serializer = UserSerializer(
            user,
            context={"request": request}
        )
        return Response(serializer.data)

    def put(self, request, slug):
        """
        Update the user's profile details
        """

        profile = self.get_object(slug)
        user = profile.user
        self.check_object_permissions(self.request, user)

        serializer = UserSerializer(
            user,
            data=request.data
        )
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
