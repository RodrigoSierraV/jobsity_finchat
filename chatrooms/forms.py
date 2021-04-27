from django import forms
from chatrooms.models import RoomChatMessage


class SendChatForm(forms.ModelForm):
    class Meta:
        model = RoomChatMessage
        fields = ('content',)
