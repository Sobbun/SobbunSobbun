from django import forms
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from phonenumber_field.formfields import PhoneNumberField
from .models import User, Profile


class SignupForm(UserCreationForm):

    phone = PhoneNumberField(region='KR')

    class Meta:
        model = User

        fields = ['username', 'password1', 'password2', 'phone']


class UpdateUserForm(forms.ModelForm):
    phone = PhoneNumberField(region='KR', required=True,)


class UpdateProfileForm(forms.Form):
    class Meta:
        model = Profile


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'users/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('users-home')
