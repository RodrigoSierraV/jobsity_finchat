from django.urls import re_path

from chatrooms import consumers

websocket_urlpatterns = [
    re_path(r'ws/chatrooms/(?P<room_id>\w+)/$', consumers.ChatConsumer.as_asgi()),
]
