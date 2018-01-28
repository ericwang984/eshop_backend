
# core
from __future__ import (
    unicode_literals, absolute_import,
)
# django
from django.db import models

# libs

# projects

# constants

 # logging
import logging
LOGGER = logging.getLogger(__name__)


class OrderQuerySet(models.QuerySet):
    """Queryset defines queryset filters describing model subsets.

    Extends:
      models.QuerySet
    """

    def active(self):
        return self.filter(is_active=True)


class OrderManager(models.Manager):
    """Model manager which gives access to filtered querysets.
    """

    def get_queryset(self):
        """Returns the manager's queryset which is a OrderQuerySet.

        Returns:
          Queryset -- OrderQuerySet
        """
        return OrderQuerySet(self.model, using=self._db)

    def active(self):
        """Returns the queryset of orders which are active.

        Returns:
          Queryset -- Orders that are active.
        """
        return self.get_queryset().active()