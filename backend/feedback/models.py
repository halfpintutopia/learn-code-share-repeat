from django.db import models
from django.contrib.auth.models import User

from videos.models import Video


class Feedback(models.Model):
    """
    Model to represent a video entry, related to :model:`auth.User` and :model:`videos.Video`
    """

    class Clarity(models.IntegerChoices):
        """
        Clarity choices
        """
        DEFAULT = 0, "Default"
        NOT_CLEAR = 1, "Not clear"
        SOMEWHAT_CLEAR = 2, "Somewhat clear"
        CLEAR = 3, "Clear"
        VERY_CLEAR = 4, "Very clear"
        EXTREMELY_CLEAR = 5, "Extremely clear"

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    video = models.ForeignKey(
        Video,
        on_delete=models.CASCADE,
        related_name="feedback"
    )
    clarity = models.IntegerField(
        choices=Clarity.choices,
        default=Clarity.DEFAULT
    )
    comment = models.TextField(
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        """
        Metaclass for the model
        """
        ordering = ["-created_at"]

    def __str__(self):
        """
        String representation of the model
        """
        return self.comment
