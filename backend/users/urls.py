from django.urls import path

from .views import RegisterListUsers, ActivateUser

urlpatterns = [
    path("api/users", RegisterListUsers.as_view(), name='user-register-list'),
    path("api/users/activate/<uidb64>/<token>/", ActivateUser.as_view(), name='activate')
]
