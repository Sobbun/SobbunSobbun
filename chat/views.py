from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden, HttpResponseNotModified
from .models import ChatRoom, ChatMessage, ChatMessageHistory
from .forms import SendMessageForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse

# Create your views here.



class ChatRoomListView(LoginRequiredMixin, generic.ListView):
    model = ChatRoom
    ordering = '-updated_at'
    context_object_name = 'rooms'
    paginate_by = 10
    template_name = 'chat/list.html'

    def get_queryset(self):
        return ChatRoom.objects.filter(participants=self.request.user)


class ChatRoomView(LoginRequiredMixin, generic.DetailView, generic.FormView):
    model = ChatRoom
    context_object_name = 'room'
    form_class = SendMessageForm
    template_name = 'chat/room.html'

    def dispatch(self, request, *args, **kwargs):
        self.object = get_object_or_404(ChatRoom, pk=kwargs['pk'])
        if not self.object.participants.contains(self.request.user):
            return HttpResponseForbidden("User is not participants")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.mark_all_as_checked()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.mark_all_as_checked()
        form = self.get_form()
        return self.form_valid(form) if form.is_valid() else self.form_invalid(form)

    def form_valid(self, form):
        message = form.save(commit=False)
        message.author = self.request.user
        message.room = self.get_object()
        message.save()
        message.refresh_from_db()
        message.checked_by.add(self.request.user)
        message.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        pk = self.object.id
        return reverse("chat:room", kwargs={"pk": pk})

    def mark_all_as_checked(self):
        messages = ChatMessage.objects.filter(room=self.object).exclude(checked_by=self.request.user)
        for message in messages:
            message.checked_by.add(self.request.user)
            message.save()

class UpdateMessageView(LoginRequiredMixin, generic.UpdateView, generic.FormView):
    model = ChatMessage
    form_class = SendMessageForm

    def dispatch(self, request, *args, **kwargs):
        self.message = get_object_or_404(ChatMessage, pk=kwargs['pk'])
        if self.message.author != self.request.user:
            return HttpResponseForbidden("User is not has a right of this message")
        return super().dispatch(request, *args, **kwargs)


    def form_valid(self, form):
        new = form.cleaned_data["content"]
        old = self.message.content

        if new == old:
            return HttpResponseNotModified()

        ChatMessageHistory.objects.create(
            message = self.message,
            content = old
        )

        self.message.content = form.cleaned_data["content"]
        self.message.save()

        return super().form_valid(form)

    def get_success_url(self) -> str:
        pk = self.object.room.id
        return reverse("chat:room", kwargs={"pk": pk})