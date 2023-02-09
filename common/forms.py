from django import forms
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from phonenumber_field.formfields import PhoneNumberField
from .models import User, Profile


class SignupForm(UserCreationForm):
    # 전화번호 Validation 기능이 있는 Field
    phone = PhoneNumberField(region='KR')

    class Meta:
        # ModelForm에서 사용할 모델
        model = User

        fields = ['username', 'password1', 'password2', 'phone']


# class UpdateUserForm(forms.ModelForm):
#     phone = PhoneNumberField(region='KR',)

#     class Meta:
#         model = User


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nickname', 'bio', 'picture']