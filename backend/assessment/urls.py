from django.urls import path

from .views import AssessmentList, AssessmentDetail

urlpatterns = [
    path("assessment/", AssessmentList.as_view(), name='list-create-assessment'),
    path("assessment/<int:pk>/", AssessmentDetail.as_view(), name='get-update-delete-assessment'),
]
