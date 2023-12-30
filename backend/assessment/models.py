from django.db import models
from django.contrib.auth import get_user_model

from videos.models import Video

User = get_user_model()


class Assessment(models.Model):
    """
    Model for assessment
    """

    class Understanding(models.IntegerChoices):
        """
        Choices for understanding
        """
        DEFAULT = 0, "Default"
        JUST_STARTING = 1, "Just starting"
        SOMEWHAT_CLEAR = 2, "Somewhat clear"
        VERY_CLEAR = 3, "Very clear"
        FULLY_UNDERSTOOD = 4, "Fully understood"

    class Proficiency(models.IntegerChoices):
        """
        Choices for proficiency
        """
        DEFAULT = 0, "Default"
        BEGINNER = 1, "Beginner"
        INTERMEDIATE = 2, "Intermediate"
        ADVANCED = 3, "Advanced"
        EXPERT = 4, "Expert"

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    video = models.OneToOneField(
        Video,
        related_name="assessments",
        on_delete=models.CASCADE
    )
    understanding = models.IntegerField(
        choices=Understanding.choices,
        default=Understanding.DEFAULT
    )
    proficiency = models.IntegerField(
        choices=Proficiency.choices,
        default=Proficiency.DEFAULT
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        """
        Metaclass for the model
        """
        ordering = ["-created_at"]
        unique_together = ["user", "video"]

        def __str__(self):
            """
            String representation of the model
            """
            return f"{self.user} - {self.video}"
