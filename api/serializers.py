from django.contrib.auth.models import User
from rest_framework import serializers
from chat.models import Room, Message


class RoomSerializer(serializers.ModelSerializer):
    users = serializers.SlugRelatedField(many=True, slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Room
        fields = ['title', 'users']


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    receiver = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    room = serializers.SlugRelatedField(many=False, slug_field='title', queryset=Room.objects.all())

    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'room', 'message', 'timestamp']
