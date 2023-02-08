from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path("", views.ChatRoomListView.as_view(), name="index"),
    path("list", views.ChatRoomListView.as_view(), name="list"),
    path("room/<int:pk>", views.ChatRoomView.as_view(), name="room"),
    path("message/<int:pk>/edit", views.UpdateMessageView.as_view(), name="edit_message")
]