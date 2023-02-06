from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed, HttpResponseForbidden, HttpResponseNotModified
from .models import ChatRoom, ChatMessage, ChatMessageHistory
from .forms import SendMessageForm

# Create your views here.

@login_required
def chatroom_list(request):
    user = request.user
    context = {
        'rooms': user.chat_rooms.all()
    }
    return render(request, 'chat/list.html', context)

@login_required
def chatroom(request, room_id):
    user = request.user
    room = get_object_or_404(ChatRoom, pk=room_id)
    
    # 참여자가 아니면 403
    if not room.participants.contains(user):
        return HttpResponseForbidden("Forbidden")

    # 기존 메세지를 전부 checked.
    messages = ChatMessage.objects.filter(room=room).exclude(checked_by=user)
    for message in messages:
        message.checked_by.add(user)
        message.save()

    context = {
        'room': room
    }
    return render(request, 'chat/room.html', context)

@login_required
def send_message(request, room_id):
    print(request.method)
    user = request.user
    room = get_object_or_404(ChatRoom, pk=room_id)

    if request.method != 'POST':
        return HttpResponseNotAllowed("Method Not Allowed")

    if not room.participants.contains(user):
        return HttpResponseForbidden("Forbidden")    
    
    form = SendMessageForm(request.POST)
    if not form.is_valid():
        return HttpResponseNotAllowed("Not allowed")

    message = form.save(commit=False)
    message.author = user
    message.room = room
    message.save()
    message.refresh_from_db()
    message.checked_by.add(user)
    message.save()

    return redirect('chat:room', room_id=room.id)

@login_required
def edit_message(request, message_id):
    print(request.method)
    user = request.user
    message = get_object_or_404(ChatMessage, pk=message_id)

    if request.method != 'POST':
        return HttpResponseNotAllowed("Method Not Allowed")

    if message.author != user:
        return HttpResponseForbidden("Forbidden")
    
    form = SendMessageForm(request.POST)
    if not form.is_valid():
        return HttpResponseNotAllowed("Not allowed")

    new = form.cleaned_data["content"]
    old = message.content 

    if new == old:
        return HttpResponseNotModified()

    ChatMessageHistory.objects.create(
        message = message,
        content = old
    )

    message.content = form.cleaned_data["content"]
    message.save()

    return redirect('chat:room', room_id=message.room.id)

