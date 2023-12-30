from django.urls import path

from .views import FeedbackList, FeedbackDetail

urlpatterns = [
    path("feedback/", FeedbackList.as_view(), name='list-create-feedback'),
    path("feedback/<int:pk>/", FeedbackDetail.as_view(), name='get-update-delete-feedback'),
]
