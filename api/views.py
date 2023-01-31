from rest_framework import viewsets
import django_filters
from .serializers import RoomSerializer, UserSerializer, MessageSerializer
from django.contrib.auth.models import User
from chat.models import Room, Message


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ["title"]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(groups__name='common')
    serializer_class = UserSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ["sender", "receiver", "room"]
