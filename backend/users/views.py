
# core
from __future__ import unicode_literals

from decimal import Decimal

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
from rest_framework.exceptions import APIException
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings



# projects
from users.models import User, Address
from users.serializers import (
    UserSerializer, AddressSerializer
)

# constants


# logging
from logging import getLogger
LOGGER = getLogger(__name__)



class CreateUserView(CreateAPIView):
    """Creating a user, either with or without a password.
    Also returns a JWT authentication token.

    Extends:
        CreateAPIView
    """
    permission_classes = (AllowAny, )
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        user = None

        email = self.request.data['email']
        first_name = self.request.data['first_name']
        last_name = self.request.data['last_name']
        print email
        print first_name
        print last_name

        deets = {}

        if 'mobile' in self.request.data:
            deets.update({'mobile': self.request.data['mobile']})

        if 'password' in self.request.data:
            password = self.request.data['password']
            user = User.objects.create_user(email, password, first_name, last_name, **deets)

        else:
            user = User.objects.create_user_random_password(email, first_name, last_name, **deets)

        # Serialize the user so that it can be posted back.
        serializer = UserSerializer(user)
        user_data = serializer.data

        # Add an authentication token
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        user_data['token'] = jwt_encode_handler(payload)

        return Response(user_data, status.HTTP_200_OK)


class AddressListCreateView(ListCreateAPIView):
    """ Used to list and create addresses of a user.
    Extends:
        ListCreateAPIView
    """
    permission_classes = (IsAuthenticated, )
    serializer_class = AddressSerializer

    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
        )


class AddressRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """ Used to retrieve update and destory address of a user.
    Extends:
        RetrieveUpdateDestroyAPIView
    """
    permission_classes = (IsAuthenticated, )
    serializer_class = AddressSerializer

    def get_object(self):
        return get_object_or_404(Address, slug=self.kwargs['address_slug'])


