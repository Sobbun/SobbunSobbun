from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "app"

post_patterns = [
    path("<int:pk>", views.PostDetailView.as_view(), name='post'),
    path("create", views.PostCreateView.as_view(), name='post_create'),
]

request_patterns = [
    path("", views.RequestListView.as_view(), name="index"),
    path("list", views.RequestListView.as_view(), name="request_list"),
    path("list/<int:post_id>", views.PostRequestListView.as_view(), name="request_post_list"),
    path("create/<int:post_id>", views.RequestCreateView.as_view(), name="request_create"),
    path("<int:pk>", views.RequestDetailView.as_view(), name="request"),
    path("<int:pk>/edit", views.RequestUpdateView.as_view(), name="request_edit"),
]

urlpatterns = [
    path("", views.index, name="index"),
    path("list", views.PostListView.as_view(), name="list"),
    path("post/", include(post_patterns)),
    path("request/", include(request_patterns))
]

