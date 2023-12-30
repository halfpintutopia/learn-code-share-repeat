from rest_framework import permissions
from django.contrib.auth import get_user_model

User = get_user_model()


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.

    Read-only permissions are allowed for any request.
    """

    def has_object_permission(self, request, view, obj):
        """
        Read permissions are allowed to any request,
        so we'll always allow GET, HEAD, or OPTIONS requests.
        """
        # GET, HEAD, OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True
        # aka post user is the authenticated user
        # here comes from model definition
        if isinstance(obj, User):
            return obj == request.user

        return obj.user == request.user
