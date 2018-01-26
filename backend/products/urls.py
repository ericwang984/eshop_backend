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
from products.views import (
    ProductCreateListView, ProductRetrieveUpdateDestroyView
)

# constants


# logging
from logging import getLogger
LOGGER = getLogger(__name__)



urlpatterns = [
    url(
        r'^$',
        ProductCreateListView.as_view(),
        name="product_create_list"
    ),

    url(
        r'^(?P<product_slug>\w{22})$',
        ProductRetrieveUpdateDestroyView.as_view(),
        name="product_retrieve_update_destroy"
    ),

]
