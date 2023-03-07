from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    name = models.CharField(_("name"), max_length=64, unique=True)
    first_name = None
    last_name = None
    description = models.TextField(blank=True)

    REQUIRED_FIELDS = ["email", "name"]
