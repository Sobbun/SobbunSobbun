from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.

@login_required
def chatroom_list(request):
    user = request.user
    context = {
        'rooms': user.chat_rooms.all()
    }
    return HttpResponse(context)