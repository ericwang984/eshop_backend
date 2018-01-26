
# core
from __future__ import (
    unicode_literals, absolute_import,
)
from decimal import Decimal as D

# libraries

# django
from django.conf import settings
from django.db import models

# libs

# project
from core.mixins import (
    TimestampBase, ShortUUIDBase, StatusBase
)
from core.constants import CATEGORIES
from products.managers import ProductManager

# constants




class Product(ShortUUIDBase, TimestampBase, StatusBase):
    """ Cart model
    Extends:
        ShortUUIDBase
        TimestampBase
        StatusBase

    Variables:
        user {foreign key} -- The user who owns the cart
    """

    category = models.CharField(max_length=2, choices=CATEGORIES.CHOICES)
    price = models.DecimalField(max_digits=15, decimal_places=8, default=D(0))
    title = models.CharField(max_length=255)
    imageUrl = models.CharField(max_length=2048)

    objects = ProductManager()

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'usersCarts'


    def __unicode__(self):
        """Unicode description."""
        return '%s %s' % (self.id, self.title)


