
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
from orders.managers import OrderManager

# constants




class Order(ShortUUIDBase, TimestampBase, StatusBase):
    """ Cart model
    Extends:
        ShortUUIDBase
        TimestampBase
        StatusBase

    Variables:
        user {foreign key} -- The user who owns the cart
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='orders_user')
    address = models.ForeignKey('users.Address', related_name='orders_address')
    cart = models.ForeignKey('carts.Cart', related_name='orders_cart')

    objects = OrderManager()

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __unicode__(self):
        """Unicode description."""
        return '%s %s' % (self.id, self.user.get_full_name())

    @property
    def total_price(self):
        """ Return the total price of the cart.
        """
        total_price = 0
        if self.cart.carts_items:
            for item in self.cart.carts_items:
                total_price += item.total_price
            return total_price
        else:
            return 0


