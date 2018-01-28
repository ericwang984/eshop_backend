
# Core
from __future__ import unicode_literals

# Lib
from random import SystemRandom
from shortuuid import decode

# Django
from django.db import models
from django_extensions.db.fields import ShortUUIDField



REFCODE_LENGTH = 6
REFCODE_CHARSET = '23478ACEFGHJKPQRSTUVWXYZ'

def generate_random_string(length=REFCODE_LENGTH, charset=REFCODE_CHARSET):
    """Generates a string of random characters to be used as a publicly available identifier.
    """
    return ''.join([
        SystemRandom(100000).choice(charset) for _ in range(0, length)
    ])


class ShortUUIDBase(models.Model):
    """Mixin to support models which have a slug which needs to be translatable into a guid.
    """

    slug = ShortUUIDField(blank=False)

    class Meta:
        abstract = True

    @property
    def guid(self):
        """Returns the slug to a UUID."""
        return decode(self.slug)

    @property
    def guid_str(self):
        """Returns the UUID as upperacse hexadecimal."""
        return self.guid.hex.upper()


class TimestampBase(models.Model):
    """Abstract model defining the create and last update time and date.
    """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    @property
    def is_new(self):
        """Returns true if the created field, which is set upon db insertion, is set.

        Returns:
            bool -- [description]
        """
        return self.created is None


class StatusBase(models.Model):
    """Abstract model defining the create and last update time and date.
    """

    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
