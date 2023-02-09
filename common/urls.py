from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'common'

urlpatterns = [
    path('login', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('signup', views.SignupView.as_view(), name='signup'),

    path('my', views.MypageView.as_view(), name='mypage'),
    path('profile/edit', views.UpdateProfileView.as_view(), name='profile_edit'),
    path('profile/new', views.SignupUpdateProfileView.as_view(), name='profile_new'),
    path('welcome', views.WelcomeView.as_view(), name='welcome'),
]