
# core
from __future__ import (
    unicode_literals, absolute_import,
)
# django
from django.db import models

# libs
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.generics import (
    get_object_or_404, GenericAPIView,
    CreateAPIView,
    ListCreateAPIView, RetrieveUpdateAPIView,
    RetrieveUpdateDestroyAPIView,
    UpdateAPIView, ListAPIView,
)
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

# projects
from orders.serializers import OrderSerializer
from orders.models import Order

# constants


# logging
from logging import getLogger
LOGGER = getLogger(__name__)


class OrderCreateListView(ListCreateAPIView):
    """ Used to list and create orders.
    Extends:
        ListCreateAPIView
    """
    permission_classes = (IsAuthenticated, )
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.active().filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user if self.request.user.is_authenticated() else None,
        )


class OrderRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """ Used to retrieve update and destory orders.
    Extends:
        RetrieveUpdateDestroyAPIView
    """
    permission_classes = (IsAuthenticated, )
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.active().filter(user=self.request.user)

    def get_object(self):
        return get_object_or_404(self.get_queryset(), slug=self.kwargs['order_slug'])

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            instance.is_active = False
            instance.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

