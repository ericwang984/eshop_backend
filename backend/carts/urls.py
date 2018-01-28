"""Urls for the Users API.
"""

# core
from __future__ import (
    unicode_literals, absolute_import,
)



# django
from django.conf.urls import url

# libs

# projects
from carts.views import (
    CartCreateListView, CartRetrieveUpdateDestroyView,
    ItemListCreateView, ItemRetrieveUpdateDestroyView
)

# constants


# logging
from logging import getLogger
LOGGER = getLogger(__name__)



urlpatterns = [
    url(
        r'^$',
        CartCreateListView.as_view(),
        name="cart_create_list"
    ),

    url(
        r'^(?P<cart_slug>\w{22})$',
        CartRetrieveUpdateDestroyView.as_view(),
        name="cart_retrieve_update_destroy"
    ),

    url(
        r'^(?P<cart_slug>\w{22})/items$',
        ItemListCreateView.as_view(),
        name="item_list_create"
    ),

    url(
        r'^(?P<cart_slug>\w{22})/items/(?P<item_slug>\w{22})$',
        ItemRetrieveUpdateDestroyView.as_view(),
        name="item_list"
    ),

]
