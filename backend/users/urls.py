from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .views.registration import RegisterUser, ActivateUser
from .views.users import ListUsers, GetUpdateUserProfileView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path("api/users", ListUsers.as_view(), name='list-users'),
    path("api/users/register", RegisterUser.as_view(), name='register-user'),
    path("api/users/activate/<uidb64>/<token>/", ActivateUser.as_view(), name='activate'),
    path("api/users/<str:slug>/", GetUpdateUserProfileView.as_view(), name='retrieve-edit-user'),
]
