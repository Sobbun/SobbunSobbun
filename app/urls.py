from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "app"
urlpatterns = [
    path("", views.index, name="index"),
    path("list", views.sobun_list, name="list"),
    path("post/<int:post_id>", views.sobun_post, name='post')
]
