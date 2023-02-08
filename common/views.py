from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import SignupForm, UpdateProfileForm

from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views import generic
from django.urls import reverse_lazy


class IndexView(generic.View):
    def get(self, request):
        return render(request, 'common/index.html')

class SignupView(generic.CreateView):
    form = SignupForm
    success_url = reverse_lazy('common:profile_edit')
    template_name = 'common/signup.html'


class UpdateProfileView(LoginRequiredMixin, generic.UpdateView):
    form = UpdateProfileForm
    success_url = reverse_lazy('common:profile_edit')
    template_name = 'common/profile/edit.html'
