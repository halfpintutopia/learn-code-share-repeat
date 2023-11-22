from django.contrib.auth import get_user_model
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from .serializers import UserProfileSerializer, UserSerializer

User = get_user_model()


class CreateAndListUsers(APIView):
    """
    View to get and update a user's profile
    """
    # serializer_class = UpdateUserProfileSerializer
    # serializer_class_output = UserSerializer
    permission_classes = {
        AllowAny,
    }

    def get(self, request):
        """
        Get the user's profile details
        """
        serializer = self.serializer_class_output(request.user)
        return Response(serializer.data)

    def post(self, request):
        """
        Update the user's profile details
        """
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
