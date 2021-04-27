from django.urls import path
from chatrooms import views


urlpatterns = [
    path(
        route='create/',
        view=views.CreateChatRoom.as_view(),
        name='create_room'
    ),
    path(
        route='list/',
        view=views.ListChatRooms.as_view(),
        name='list_rooms'
    ),
    path(
        route='<str:room_id>/',
        view=views.send_messages_view,
        name='private_room'
    )
]
