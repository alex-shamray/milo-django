import random

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
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

    def get_age(self):
        today = timezone.now().date()
        try:  # raised when birth day is February 29 and the current year is not a leap year
            birthday = self.birthday.replace(year=today.year)
        except ValueError:
            birthday = self.birthday.replace(year=today.year, day=self.birthday.day - 1)

        if birthday > today:
            return today.year - self.birthday.year - 1
        else:
            return today.year - self.birthday.year

    def get_eligibility_status(self):
        """
        Returns "allowed" if the user is older than 13 years otherwise returns "blocked"
        """
        return 'allowed' if self.birthday and self.get_age() > 13 else 'blocked'

    def get_bizzfuzz_status(self):
        """
        Returns the BizzFuzz result of the random number that was generated for the user.

        The BizzFuzz specification is that for multiples of 3 it returns "Bizz" instead of
        the number and for the multiples of 5 it returns "Fuzz". For numbers which are
        multiples of both 3 and 5 it returns "BizzFuzz".
        """
        if self.random_num % 3 == 0 and self.random_num % 5 == 0:
            return 'BizzFuzz'
        elif self.random_num % 3 == 0:
            return 'Bizz'
        elif self.random_num % 5 == 0:
            return 'Fuzz'
        return self.random_num
