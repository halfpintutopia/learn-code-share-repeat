from django.db import models
from django.conf import settings

from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    """
    This Profile model is a OneToOneField to the User model that will be
    created when a user registers. It will contain additional information
    about the user.
    """

    class Pronouns(models.TextChoices):
        FEMININE = "FEM", _("she/her")
        MASCULINE = "MAS", _("he/him")
        NEUTRAL = "NEU", _("they/them")
        NON_BINARY = "NON", _("xe/xem")

    user = models.OneToOneField(
        verbose_name="user",
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_profile"
    )
    location = models.CharField(
        max_length=255,
        null=True
    )
    pronoun = models.CharField(
        max_length=3,
        choices=Pronouns.choices,
        default="Please select"
    )
    website = models.URLField(blank=True, null=True)
    social = models.JSONField(blank=True, null=True)
    image = models.ImageField(
        upload_to="profile_image",
        blank=True,
        null=True
    )
    background_image = models.ImageField(
        upload_to="profile_background_image",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.user.username
