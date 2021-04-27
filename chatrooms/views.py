from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from chatrooms.models import ChatRoom, RoomChatMessage


class ListChatRooms(LoginRequiredMixin, ListView):
    model = ChatRoom
    paginate_by = 50
    ordering = 'created_at'
    template_name = 'chatrooms/list_chatrooms.html'
    context_object_name = 'chatrooms_list'


@login_required
def send_messages_view(request, room_id):
    messages = RoomChatMessage.objects.filter(room_id=room_id).order_by('-timestamp')[:50]
    return render(request, 'chatrooms/room.html', {
        'room_id': room_id,
        'user': str(request.user),
        'messages': reversed(messages)
    })


class CreateChatRoom(LoginRequiredMixin, CreateView):
    model = ChatRoom
    fields = ('name',)
    template_name = 'chatrooms/create_chatroom.html'
    success_url = reverse_lazy('chatrooms:list_rooms')

    def form_valid(self, form):
        room = form.save(commit=False)
        room.creator = self.request.user
        room.save()
        return super().form_valid(form)
