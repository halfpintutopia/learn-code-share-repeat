from django.urls import path

from .views import CreateAndListUsers

urlpatterns = [
    path("api/users", CreateAndListUsers.as_view(), name='user-create-list')
]
