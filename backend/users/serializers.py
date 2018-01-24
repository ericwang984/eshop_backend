"""Serializers for the Users API.
"""

# core
from __future__ import unicode_literals

# libs
from rest_framework import serializers

# projects
from users.models import User


# logging
from logging import getLogger
LOGGER = getLogger(__name__)



class UserSerializer(serializers.ModelSerializer):
    """Serializer which creates and updates the user."""

    password = serializers.CharField(
        write_only=True,
        required=False
    )

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'slug',

            'date_joined',
            'last_login',

            'is_staff',
            'is_new',

            'first_name',
            'last_name',

            'mobile',
            'dob',
            'gender',

            'password',
            'has_password',
            'has_set_password',
        )
        read_only_fields = (
            'id',
            'slug',
            'date_joined',
            'last_login',
        )
        required_fields = (
            'email',
            'first_name',
            'last_name',
        )




