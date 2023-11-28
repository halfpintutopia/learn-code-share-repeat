from .models import Profile
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save

User = get_user_model()


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Automatically create related record for profile instance when a new User instance is created
    """
    if created:
        Profile.objects.create(user=instance)
