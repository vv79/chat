from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    title = models.CharField(max_length=255)
    users = models.ManyToManyField(User, through='RoomUser')

    def str(self):
        return self.title


class RoomUser(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "room_users"


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room')
    message = models.CharField(max_length=1200)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.message

    class Meta:
        ordering = ('timestamp',)
