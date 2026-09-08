# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserRole(models.TextChoices):
    ADMIN = "ADMIN", "管理者"
    EDITOR = "EDITOR", "編集者"
    VIEWER = "VIEWER", "閲覧者"


class User(AbstractUser):
    role = models.CharField(
        max_length=10,
        choices=UserRole.choices,
        default=UserRole.VIEWER,
    )
