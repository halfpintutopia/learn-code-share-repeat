from .models import Profile
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save

from .tokens import account_activation_token

User = get_user_model()


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Automatically create related record for profile instance when a new User instance is created
    """
    if created:
        profile = Profile.objects.create(user=instance)
        profile.is_email_verified = False
        profile.email_verification_token = account_activation_token.make_token(instance)
        profile.save()
