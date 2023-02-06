from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'common'

urlpatterns = [
    path('login', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('signup', views.signup, name='signup'),

    path('profile/edit', views.profile_update, name='profile_edit'),

    path("event", views.event_list, name="event_index"),
    path("event/list", views.event_list, name="event_list"),
    path("event/post/<int:event_id>", views.event_post, name='event_post')
]