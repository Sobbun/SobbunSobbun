from django import forms
from django.urls import reverse_lazy

from .models import ChatMessage, ChatMessageHistory


class SendMessageForm(forms.ModelForm):
    class Meta:
        model = ChatMessage
        fields = ['content']
