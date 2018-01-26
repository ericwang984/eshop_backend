"""Serializers for the Users API.
"""

# core
from __future__ import (
    unicode_literals, absolute_import,
)

# libs
from rest_framework import serializers

# projects
from carts.models import Cart


# logging
from logging import getLogger
LOGGER = getLogger(__name__)



class CartSerializer(serializers.ModelSerializer):
    """Serializer for product model queries.

    Extends:
        serializers.ModelSerializer
    """

    class Meta:
        model = Cart
        fields = (
            'slug',
            'created',
            'updated',
            'user'
        )

        read_only_fields = (
            'slug',
            'created',
            'updated',
            'user'
        )

