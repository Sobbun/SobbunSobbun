    
from django.urls import path
from . import views

app_name = 'event'

urlpatterns = [
    path("", views.EventListView.as_view(), name="index"),
    path("list", views.EventListView.as_view(), name="list"),
    path("id/<int:pk>", views.EventDetailView.as_view(), name='post')
]