"""Serializers for the Users API.
"""

# core
from __future__ import (
    unicode_literals, absolute_import,
)

# libs
from rest_framework import serializers

# projects
from products.models import Product


# logging
from logging import getLogger
LOGGER = getLogger(__name__)


class ProductSerializer(serializers.ModelSerializer):
    """Serializer for product model queries.

    Extends:
        serializers.ModelSerializer
    """

    class Meta:
        model = Product

        fields = (
            'slug',
            'category',
            'price',
            'title',
            'imageUrl',
            'created',
            'updated'
        )

        read_only_fields = (
            'slug',
            'created',
            'updated'
        )
