from django.urls import path

from .views.registration import RegisterUser, ActivateUser
from .views.users import ListUsers

urlpatterns = [
    path("api/users", ListUsers.as_view(), name='list-users'),
    path("api/users/register", RegisterUser.as_view(), name='register-user'),
    path("api/users/activate/<uidb64>/<token>/", ActivateUser.as_view(), name='activate')
]
