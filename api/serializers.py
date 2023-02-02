from django.contrib.auth.models import User
from rest_framework import serializers
from chat.models import Room, Message


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'title', 'date_created', 'slug', 'users']


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password']


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    receiver = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    room = serializers.SlugRelatedField(many=False, slug_field='title', queryset=Room.objects.all())

    class Meta:
        model = Message
        fields = ['id', 'sender', 'receiver', 'room', 'message', 'date_created']
