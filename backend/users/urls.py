"""Urls for the Users API.
"""

# core
from __future__ import unicode_literals



# django
from django.conf.urls import url

# libs
from rest_framework_jwt.views import (
    obtain_jwt_token, refresh_jwt_token, verify_jwt_token
)

# projects
from users.views import (
    CreateUserView, AddressListCreateView,
    AddressRetrieveUpdateDestroyView
)

# constants


# logging
from logging import getLogger
LOGGER = getLogger(__name__)



urlpatterns = [

    url(
        r'^token/obtain$',
        obtain_jwt_token,
        name='obtain_token'
    ),

    url(
        r'^token/refresh$',
        refresh_jwt_token,
        name='refresh_token'
    ),

    url(
        r'^token/verify$',
        verify_jwt_token,
        name='verify_token'
    ),

    url(
        r'^$',
        CreateUserView.as_view(),
        name="user_create"
    ),

    url(
        r'^address$',
        AddressListCreateView.as_view(),
        name="address_list_create"
    ),

    url(
        r'^address/(?P<address_slug>\w{22})$',
        AddressRetrieveUpdateDestroyView.as_view(),
        name="address_retrieve_update_destroy"
    ),
    # url(
    #     r'^users$',
    #     UsersList.as_view(),
    #     name="list_userss"
    #     ),

]
