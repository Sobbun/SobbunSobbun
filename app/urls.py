from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "app"

post_patterns = [
    path("<int:pk>", views.PostDetailView.as_view(), name='post'),
    path("create", views.PostCreateView.as_view(), name='post_create'),
]

request_patterns = [
    path("", views.RequestListView.as_view(), name="request_index"),
    path("list", views.RequestListView.as_view(), name="request_list"),
    path("list/<int:post_id>", views.PostRequestListView.as_view(), name="request_post_list"),
    path("create/<int:post_id>", views.RequestCreateView.as_view(), name="request_create"),
    path("<int:pk>", views.RequestDetailView.as_view(), name="request"),
    path("<int:pk>/edit", views.RequestUpdateView.as_view(), name="request_edit"),
]

rate_patterns = [
    path("", views.RateUserListView.as_view(), name="rate_index"),
    path("list", views.RateUserListView.as_view(), name="rate_list"),
    path("list/<int:pk>", views.RateListView.as_view(), name="rate_post_list"),
    path("create/<int:sobun_id>", views.RateCreateView.as_view(), name="rate_create"),
    path("<int:pk>", views.RateDetailView.as_view(), name="rate"),
]

temp_patterns = [
    path("request_create/<int:sobun_id>", views.temp_request_chat_create, name="temp_request_chat_create"),
    path("request_complete/<int:sobun_id>/redirect/<int:chat_id>", views.temp_request_chat_complete, name="temp_request_chat_complete")
]

urlpatterns = [
    path("", views.index, name="index"),
    path("list", views.PostListView.as_view(), name="list"),
    path("post/", include(post_patterns)),
    path("request/", include(request_patterns)),
    path("rate/", include(rate_patterns)),

    path("not_production_ready/temp/", include(temp_patterns))
]

