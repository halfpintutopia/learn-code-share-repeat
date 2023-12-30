from cloudinary_storage.storage import VideoMediaCloudinaryStorage, RawMediaCloudinaryStorage

from django.db import models
from django.contrib.auth.models import User


class Video(models.Model):
    """
    Model to represent a video entry
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="videos"
    )
    image = models.ImageField(
        verbose_name="Video Screenshot",
        upload_to="video_screenshot",
        storage=RawMediaCloudinaryStorage(),
        blank=True
    )
    video = models.FileField(
        verbose_name="Video",
        upload_to="videos",
        storage=VideoMediaCloudinaryStorage(),
        blank=True
    )
    title = models.CharField(
        max_length=255
    )
    technology_versions = models.CharField(
        max_length=255,
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now_add=True
    )
