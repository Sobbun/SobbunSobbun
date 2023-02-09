from .forms import SignupForm, UpdateProfileForm
from django.contrib.auth import get_user_model, login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic
from django.urls import reverse, reverse_lazy
from .models import Profile

User = get_user_model()

class IndexView(generic.View):
    def get(self, request):
        return render(request, 'common/index.html')

class MypageView(generic.View):
    def get(self, request):
        return render(request, 'common/mypage.html')

class SignupView(generic.CreateView):
    #model = User
    form_class = SignupForm
    template_name = 'common/signup.html'

    def form_valid(self, form):
        _ = super().form_valid(form)
        form.save()
        username = form.cleaned_data['username']
        raw_password = form.cleaned_data['password1']
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        return _

    def get_success_url(self) -> str:
        return reverse('common:profile_edit') + '?next=/common/logout'

class UpdateProfileView(LoginRequiredMixin, generic.UpdateView):
    form_class = UpdateProfileForm
    success_url = reverse_lazy('common:profile_edit')
    template_name = 'common/profile/edit.html'

    def get_object(self):
        return self.request.user.profile # type: ignore

    def get_success_url(self) -> str:
        next = self.request.GET.get("next")
        if next:
            return next
        return super().get_success_url()