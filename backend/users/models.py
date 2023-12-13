from django.db import models
from django.conf import settings

from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import slugify


class Profile(models.Model):
    """
    This Profile model is a OneToOneField to the User model that will be
    created when a user registers. It will contain additional information
    about the user.
    """

    class Pronouns(models.TextChoices):
        NONE = "NOT", _("prefer not to say")
        FEMININE = "FEM", _("she/her")
        MASCULINE = "MAS", _("he/him")
        NEUTRAL = "NEU", _("they/them")
        NON_BINARY = "NON", _("xe/xem")

    user = models.OneToOneField(
        verbose_name="User Profile",
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_profile"
    )
    location = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    pronoun = models.CharField(
        max_length=3,
        choices=Pronouns.choices,
        default=Pronouns.NONE
    )
    personal_website = models.URLField(
        verbose_name="Personal website",
        blank=True,
        null=True
    )
    social_links = models.JSONField(
        verbose_name="Social links",
        blank=True,
        null=True
    )
    image = models.ImageField(
        verbose_name="Profile image",
        upload_to="profile_image",
        blank=True,
        null=True
    )
    background_image = models.ImageField(
        verbose_name="Background image",
        upload_to="profile_background_image",
        blank=True,
        null=True
    )
    joined_date = models.DateTimeField(
        verbose_name="joined_date",
        auto_now_add=True,
        null=True
    )
    is_email_verified = models.BooleanField(
        default=False
    )
    email_verification_token = models.CharField(
        max_length=225
    )
    slug = models.SlugField(
        max_length=225,
        unique=True
    )

    def save(self, *args, **kwargs):
        """
        Override the default save method so that the slug
        field is automatically populated with the user's username
        """
        if not self.slug:
            slug = slugify(f"{self.user.username}")

            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        """
        String representation of the user's profile
        """
        return f"{self.user}"
