from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import UserManager


class User(AbstractUser):
    username = models.CharField(
        max_length=6,
        unique=True,
        blank=False,
        default="",
        error_messages={
            "required": "Username must be provided.",
            "unique": "A user with that username already exists.",
            "max-length": "A username can have a maximum length of 6",
        },
    )
    email = models.EmailField(
        unique=True,
        blank=False,
        error_messages={
            "unique": "A user with that email already exists.",
        },
    )

    REQUIRED_FIELDS = ["email"]

    def __unicode__(self):
        return self.email

    objects = UserManager()
