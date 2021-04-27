from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ChatRoom(models.Model):
    """
    A private room for people to chat in.
    """
    name = models.CharField(primary_key=True, max_length=100, help_text='Less than 100 characters')
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)


class RoomChatMessage(models.Model):
    """
    Chat message created by a user inside a Room
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(unique=False, blank=False,)

    def __str__(self):
        return self.content

