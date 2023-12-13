from django.contrib.auth import get_user_model

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from ..serializers import UserProfileSerializer
from ..models import Profile

User = get_user_model()


# @route
class ListUsers(APIView):
    """
    View to get and update a user's profile
    """
    permission_classes = [
        IsAuthenticatedOrReadOnly
    ]

    @staticmethod
    def get(request):
        """
        Get the user's profile details
        """
        profiles = Profile.objects.all()
        serializer = UserProfileSerializer(profiles, many=True)
        return Response(serializer.data)
