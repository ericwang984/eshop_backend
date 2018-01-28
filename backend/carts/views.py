
# core
from __future__ import (
    unicode_literals, absolute_import,
)
# django

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
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

# projects
from carts.models import (
    Cart, CartItem
)
from carts.serializers import (
    CartSerializer, ItemSerializer
)

# projects

# constants


# logging
from logging import getLogger
LOGGER = getLogger(__name__)


class CartCreateListView(ListCreateAPIView):
    """ Used to list and create carts.
    Extends:
        ListCreateAPIView
    """
    permission_classes = (IsAuthenticated, )
    serializer_class = CartSerializer

    def get_queryset(self):
        return Cart.objects.active().filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user if self.request.user.is_authenticated() else None,
        )

class CartRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """ Used to retrieve update and destory carts.
    Extends:
        RetrieveUpdateDestroyAPIView
    """
    permission_classes = (IsAuthenticated, )
    serializer_class = CartSerializer

    def get_queryset(self):
        return Cart.objects.active().filter(user=self.request.user)

    def get_object(self):
        return get_object_or_404(
            self.get_queryset(),
            slug=self.kwargs['cart_slug']
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            instance.is_active = False
            instance.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ItemListCreateView(ListCreateAPIView):
    """ Used to list and create items for a cart.
    Extends:
        ListCreateAPIView
    """
    permission_classes = (IsAuthenticated, )
    serializer_class = ItemSerializer

    def get_cart(self):
        active_carts = Cart.objects.active().filter(user=self.request.user)
        return get_object_or_404(active_carts, slug=self.kwargs['cart_slug'])

    def get_queryset(self):
        return CartItem.objects.filter(cart=self.get_cart())

    def perform_create(self, serializer):
        serializer.save(
            cart=self.get_cart(),
        )


class ItemRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """ Used to retrieve update and destory items in a cart.
    Extends:
        RetrieveUpdateDestroyAPIView
    """
    permission_classes = (IsAuthenticated, )
    serializer_class = ItemSerializer

    def get_cart(self):
        active_carts = Cart.objects.active().filter(user=self.request.user)
        return get_object_or_404(active_carts, slug=self.kwargs['cart_slug'])

    def get_queryset(self):
        return CartItem.objects.filter(cart=self.get_cart())

    def get_object(self):
        return get_object_or_404(self.get_queryset(), slug=self.kwargs['item_slug'])
