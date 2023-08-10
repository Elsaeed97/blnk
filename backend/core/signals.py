from django.contrib.auth.models import Group
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import CustomUser


@receiver(post_migrate)
def create_user_groups(sender, **kwargs):
    """
    This Signal Creates Groups for custom user choices if they don't exists
    """
    role_choices = [choice[0] for choice in CustomUser.ROLE_CHOICES]

    for role_choice in role_choices:
        Group.objects.get_or_create(name=role_choice)
