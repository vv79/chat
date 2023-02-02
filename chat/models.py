from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Room(models.Model):
    title = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(default="", null=False)
    users = models.ManyToManyField(User, through='RoomUser')

    class Meta:
        ordering = ('date_created', 'title', )

    def str(self):
        return self.title

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class RoomUser(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "chat_room_users"


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room')
    message = models.CharField(max_length=1200)
    date_created = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.message

    class Meta:
        ordering = ('date_created',)
