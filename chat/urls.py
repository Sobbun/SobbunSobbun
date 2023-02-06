from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'chat'

urlpatterns = [
    path("", views.chatroom_list, name="index"),
    path("list", views.chatroom_list, name="list"),
    path("room/<int:room_id>", views.chatroom, name="room"),
    path("room/<int:room_id>/send", views.send_message, name="send_message"),
    path("message/<int:message_id>/edit", views.edit_message, name="edit_message")
]