from rest_framework import viewsets
import django_filters
from .serializers import RoomSerializer, UserSerializer, MessageSerializer
from django.contrib.auth.models import User
from chat.models import Room, Message
from django.db.models import Q


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
    # filterset_fields = ["sender", "receiver", "room"]

    def get_queryset(self):
        queryset = Message.objects.all()

        if 'room' in self.request.GET:
            queryset = queryset.filter(room__id=self.request.GET['room'])

        if 'sender' in self.request.GET and 'receiver' in self.request.GET:
            queryset = queryset.filter(
                Q(sender__id__in=[self.request.GET['sender'], self.request.GET['receiver']]) |
                Q(receiver__id__in=[self.request.GET['sender'], self.request.GET['receiver']])
            )
        elif 'sender' in self.request.GET:
            queryset = queryset.filter(
                Q(sender__id=self.request.GET['sender']) |
                Q(receiver__id=self.request.GET['sender'])
            )
        elif 'receiver' in self.request.GET:
            queryset = queryset.filter(
                Q(sender__id=self.request.GET['receiver']) |
                Q(receiver__id=self.request.GET['receiver'])
            )

        return queryset

