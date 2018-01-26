
# core
from __future__ import (
    unicode_literals, absolute_import,
)

# libraries

# django
from django.conf import settings
from django.db import models

# libs

# project
from core.mixins import (
    TimestampBase, ShortUUIDBase, StatusBase
)
from carts.managers import CartManager

# constants




class Cart(ShortUUIDBase, TimestampBase, StatusBase):
    """ Cart model
    Extends:
        ShortUUIDBase
        TimestampBase
        StatusBase

    Variables:
        user {foreign key} -- The user who owns the cart
    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="carts_user")
    cartsitems = models.ManyToManyField(
        'products.Product',
        through='CartItem',
        through_fields=('cart', 'item'),
    )

    objects = CartManager()

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'usersCarts'


    def __unicode__(self):
        """Unicode description."""
        return '%s' % (self.id)



class CartItem(TimestampBase):
    """ A table connect cart and product.
    Extends:
        TimestampBase

    Variables:
        cart {foreign key} -- The user who owns the cart
    """
    cart = models.ForeignKey('Cart', related_name="items_cart")
    item = models.ForeignKey('products.Product', related_name="carts_item")

    class Meta:
        verbose_name = 'Cart item'
        verbose_name_plural = 'Cart itmes'


    def __unicode__(self):
        """Unicode description."""
        return '%s %s %s' % (self.id, self.cart, self.item.title)
