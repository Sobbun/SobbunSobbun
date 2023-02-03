from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "app"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:post_id>", views.sobun_post, name='post')
]
