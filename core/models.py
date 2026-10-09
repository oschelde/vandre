from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import AbstractUser
from django.db import models


class BaseTimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser, BaseTimestampedModel):
    """
    Custom user model extending the default Django user model.
    """

    phone = models.CharField(max_length=20, blank=True, verbose_name=_("Phone"))

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_email(self):
        return self.email

    def __str__(self):
        return self.username
