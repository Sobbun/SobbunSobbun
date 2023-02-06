    
from django.urls import path
from . import views

app_name = 'event'

urlpatterns = [
    path("", views.event_list, name="index"),
    path("list", views.event_list, name="list"),
    path("id/<int:event_id>", views.event_post, name='post')
]