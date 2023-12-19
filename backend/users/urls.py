from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .views.registration import RegisterUser, ActivateUser
from .views.users import ListUsers, GetUpdateUserView

urlpatterns = [
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path("users/", ListUsers.as_view(), name='list-users'),
    path("users/register/", RegisterUser.as_view(), name='register-user'),
    path("users/activate/", ActivateUser.as_view(), name='activate'),
    path("users/<str:slug>/", GetUpdateUserView.as_view(), name='retrieve-edit-user'),
]
