from django.db.models import Count, Max
from django.contrib.auth import get_user_model
from django.http import Http404
from rest_framework import filters

from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from app.permissons import IsOwnerOrReadOnly
from ..models import Profile

from ..serializers import UserSerializer

User = get_user_model()


# @route
class ListUsers(ListAPIView):
    """
    View to get all users' profiles
    """
    permission_classes = [
        IsAuthenticatedOrReadOnly
    ]
    queryset = User.objects.annotate(
        videos_count=Count('videos', distinct=True),
        latest_video_created_at=Max('videos__created_at')
    ).order_by('-latest_video_created_at')
    serializer_class = UserSerializer
    filter_backends = [
        filters.OrderingFilter,
    ]
    ordering_fields = [
        'videos_count',
        'latest_video_created_at',
    ]


class GetUpdateUserView(RetrieveUpdateAPIView):
    """
    View to get and update user's profile
    """
    permission_classes = [
        IsOwnerOrReadOnly
    ]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        """
        Helper method to get the user's profile
        """
        try:
            slug = self.kwargs.get('slug')
            profile = Profile.objects.get(slug=slug)
            self.check_object_permissions(self.request, profile.user)

            user = User.objects.annotate(
                videos_count=Count('videos', distinct=True),
                latest_video_created_at=Max('videos__created_at')
            ).get(id=profile.user.id)

            return user
        except Profile.DoesNotExist:
            raise Http404
