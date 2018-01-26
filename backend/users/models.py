
# core
from __future__ import (
    unicode_literals, absolute_import,
)

# libraries

# django
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from django_extensions.db.fields import ShortUUIDField
from django.utils.translation import ugettext_lazy as _

# libs

# project
from users.managers import UserManager
from core.mixins import (
    TimestampBase, ShortUUIDBase, StatusBase
)


# constants
from core.constants import (
    GENDER
)




class User(AbstractBaseUser, PermissionsMixin, ShortUUIDBase, TimestampBase, StatusBase):
    """[summary]

    [description]

    Extends:
        AbstractBaseUser
        PermissionsMixin
        ShortUUIDBase

    Variables:
        is_staff {bool} -- [description]
        is_active {bool} -- [description]
        date_joined {[type]} -- [description]
        email {[type]} -- [description]
        first_name {[type]} -- [description]
        last_name {[type]} -- [description]
        mobile {[type]} -- [description]
        objects {[type]} -- UserManager
    """

    # regular django (admin) fields
    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text='Designates whether the user appears under Customer or'
        ' Staff and can log into this admin site')
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    # basic user profile fields
    email = models.EmailField(
        max_length=255,
        unique=True,
        db_index=True,
    )

    has_set_password = models.BooleanField(default=False)

    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)

    mobile = models.CharField(max_length=20, blank=True)

    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, default=GENDER.UNSPECIFIED, choices=GENDER.CHOICES)

    is_vip = models.BooleanField(default=False, null=False, blank=False)

    # use a new object manager
    objects = UserManager()

    # required for auth
    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ['email']

    def __unicode__(self):
        """Unicode description."""
        return '%s %s%s' % (self.id, self.get_full_name(), (' [%s]' % self.email) if self.email else '')

    def get_full_name(self):
        """Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Returns the short name for the user."""
        return self.first_name

    @property
    def username(self):
        return self.email

    @property
    def has_password(self):
        return self.password != ''

