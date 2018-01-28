
# core
from __future__ import (
    unicode_literals, absolute_import,
)

# libs
from rest_framework import serializers

# projects
from carts.models import (
    Cart, CartItem
)
from products.serializers import ProductSerializer


# logging
from logging import getLogger
LOGGER = getLogger(__name__)



class ItemSerializer(serializers.ModelSerializer):
    """Serializer for cartitem model queries.

    Extends:
        serializers.ModelSerializer
    """
    class Meta:
        model = CartItem
        fields = (
            'id',
            'slug',
            'item',
            'created',
            'updated',
            'quantity',
            'total_price'
        )

        read_only_fields = (
            'id',
            'slug',
            'item',
            'created',
            'updated',
            'total_price'
        )

class CartSerializer(serializers.ModelSerializer):
    """Serializer for product model queries.

    Extends:
        serializers.ModelSerializer
    """
    items = ItemSerializer(many=True, source="items_cart")

    class Meta:
        model = Cart
        fields = (
            'id',
            'slug',
            'created',
            'updated',
            'items',
            'user'
        )

        read_only_fields = (
            'id',
            'slug',
            'created',
            'updated',
            'user'
        )
