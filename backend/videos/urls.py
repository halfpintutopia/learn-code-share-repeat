from django.urls import path

from .views import VideoList, VideoDetail

urlpatterns = [
    path("videos/", VideoList.as_view(), name='list-create-video'),
    path("videos/<int:pk>", VideoDetail.as_view(), name='get-update-delete-video'),
]
