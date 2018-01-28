
# core
from __future__ import (
    unicode_literals, absolute_import,
)

# libs
from rest_framework import serializers

# projects
from orders.models import Order


# logging
from logging import getLogger
LOGGER = getLogger(__name__)


class OrderSerializer(serializers.ModelSerializer):
    """Serializer for order model queries.

    Extends:
        serializers.ModelSerializer
    """

    class Meta:
        model = Order

        fields = (
            'id',
            'slug',
            'created',
            'updated',
            'user',
            'address',
            'cart',
            'total_price'
        )

        read_only_fields = (
            'id',
            'slug',
            'created',
            'updated',
            'user',
            'total_price'
        )
