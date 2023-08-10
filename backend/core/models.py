from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from model_utils import Choices
from django.utils.translation import gettext_lazy as _
import jwt
from rest_framework_simplejwt.tokens import RefreshToken

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("The Username field must be set")

        user = self.model(username=username, **extra_fields)
        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("is_staff must = True for Superuser")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("is_superuser must = True for Superuser")

        return self.create_user(username, password, **extra_fields)


class CustomUser(AbstractUser):
    """
    Edit the Abstract user to add roles for users
    """

    ROLE_CHOICES = Choices(
        ("LOAN_PROVIDER", _("Loan Provider")),
        ("LOAN_CUSTOMER", _("Loan Customer")),
        ("BANK_PERSONNEL", _("Bank Personnel")),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
    )
    USERNAME_FIELD = "username"
    objects = CustomUserManager()
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_users",
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )

    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_users",
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )
