import random

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


def randint():
    return random.randrange(1, 101)


class User(AbstractUser):
    """
    Users within the Django authentication system are represented by this
    model.

    Username, password and email are required. Other fields are optional.
    """

    birthday = models.DateField(_('birthday'), blank=True, null=True)
    random_num = models.IntegerField(_('random number'), default=randint)
