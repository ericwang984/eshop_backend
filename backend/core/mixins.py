"""Mixin to support models which have a refcode.
"""

from __future__ import unicode_literals

from random import SystemRandom

# from django.conf import settings
# from django.db import models

# from users.models.nouns import NOUNS
# from users.models.adjectives import ADJECTIVES


REFCODE_LENGTH = 6
REFCODE_CHARSET = '23478ACEFGHJKPQRSTUVWXYZ'

def generate_random_string(length=REFCODE_LENGTH, charset=REFCODE_CHARSET):
    """Generates a string of random characters to be used as a publicly available identifier.
    """
    return ''.join([
        SystemRandom(100000).choice(charset) for _ in range(0, length)
    ])