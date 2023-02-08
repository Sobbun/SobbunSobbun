from .forms import SignupForm, UpdateProfileForm
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

User = get_user_model()

class IndexView(generic.View):
    def get(self, request):
        return render(request, 'common/index.html')

class SignupView(generic.CreateView):
    #model = User
    form_class = SignupForm
    success_url = reverse_lazy('common:profile_edit')
    template_name = 'common/signup.html'


class UpdateProfileView(LoginRequiredMixin, generic.UpdateView):
    form = UpdateProfileForm
    success_url = reverse_lazy('common:profile_edit')
    template_name = 'common/profile/edit.html'
