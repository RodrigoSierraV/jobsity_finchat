import json
from channels.generic.websocket import AsyncWebsocketConsumer
from chatrooms.models import RoomChatMessage, ChatRoom
from django.contrib.auth.models import User
from asgiref.sync import sync_to_async


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = 'chat_{}'.format(self.room_name)

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        user_name = text_data_json['user']
        user = await sync_to_async(User.objects.get, thread_sensitive=True)(username=user_name)
        room = await sync_to_async(ChatRoom.objects.get, thread_sensitive=True)(name=self.room_name)

        if not message.startswith('/stock='):
            await sync_to_async(RoomChatMessage.objects.create, thread_sensitive=True)(
                user=user,
                room=room,
                content=message
            )
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user': user_name
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        user = event['user']
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'user': user
        }))
