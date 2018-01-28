
# core
from __future__ import (
    unicode_literals, absolute_import,
)



# django
from django.conf.urls import url

# libs

# projects
from orders.views import (
    OrderCreateListView, OrderRetrieveUpdateDestroyView
)

# constants


# logging
from logging import getLogger
LOGGER = getLogger(__name__)



urlpatterns = [
    url(
        r'^$',
        OrderCreateListView.as_view(),
        name="order_create_list"
    ),

    url(
        r'^(?P<order_slug>\w{22})$',
        OrderRetrieveUpdateDestroyView.as_view(),
        name="order_retrieve_update_destroy"
    ),

]
