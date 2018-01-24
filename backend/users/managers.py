
# core
from __future__ import unicode_literals

from datetime import datetime, timedelta
from random import randint

# django
from django.contrib.auth.models import BaseUserManager
from django.utils import timezone

# libs
import names

# projects
from core.mixins import generate_random_string

# constants
from core.constants import (
    GENDER, DAYS_PER_YEAR, MONTHS_PER_YEAR
)

 # logging
import logging
LOGGER = logging.getLogger(__name__)


class UserManager(BaseUserManager):

    def create_user_random_password(self, email, first_name, last_name, **extra_fields):
        """Creates and saves a User with the given email and a generates a random password.

        Arguments:
            email {str} -- username
            **extra_fields {dict} -- Other user model fields that can be passed in to set the user

        Keyword Arguments:

        Returns:
            User -- user instance
        """
        return self.create_user(email, generate_random_string(24), first_name, last_name, has_set_password=False, **extra_fields)

    def create_user(self, email, password, first_name, last_name, has_set_password=True, **extra_fields):
        """Creates and saves a User with the given email and password.

        Arguments:
            email {str} -- username
            password {str} -- forreals
            **extra_fields {dict} -- Other user model fields that can be passed in to set the user

        Keyword Arguments:

        Returns:
            User -- user instance
        """

        now = timezone.now()
        email = BaseUserManager.normalize_email(email.lower())

        user = self.model(email=email, first_name=first_name, last_name=last_name,
                          is_staff=False, is_active=True, is_superuser=False,
                          is_new=True, has_set_password=has_set_password,
                          last_login=now, date_joined=now, **extra_fields)
        user.set_password(password)
        user.save()

        return user


    def create_superuser(self, email, password, first_name='Super', last_name='User', **extra_fields):
        """Creates a user with elevated privileges.

        Arguments:
            email {str} -- username
            password {str} -- forreals
            **extra_fields {dict} -- Other user model fields that can be passed in to set the user

        Returns:
            User -- user instance
        """
        user = self.create_user(email.lower(), password, first_name, last_name, **extra_fields)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.has_set_password = password != ''
        user.save(using=self._db)

        return user


    def generate_random_user(self, first_name=None, last_name=None,
            gender=None, dob=None,
            signup_refcode=None,
            create_token=False):
        """Generates a random user.

        Returns:
            user -- User
        """

        if gender is None:
            gender = GENDER.MALE

        if first_name is None:
            first_name = names.get_first_name(gender=('male' if gender == GENDER.MALE else 'female'))

        if last_name is None:
            last_name = names.get_last_name()

        today = datetime.today()
        if dob is None:
            dob = today - timedelta(days=randint(int(30 * DAYS_PER_YEAR), int(40 * DAYS_PER_YEAR)))

        telephone = '0' + str(randint(400000000, 499999999))
        email = ('dan+%s.%s@.com.au' % (first_name, last_name)).lower()

        # create a user
        user = self.create_user(
            email,
            'password',
            **{
                'first_name': first_name,
                'last_name': last_name,
                'mobile': telephone,
                'dob': dob,
                'signup_refcode': signup_refcode
            }
        )

        return user

    @property
    def total_users_signed_up_ever(self):
        """Returns the total users signed up ever.
        Returns:
          The count of total users signed up ever.
        """
        return self.count()
