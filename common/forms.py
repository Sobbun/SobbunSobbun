from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField
from .models import User

class UserForm(UserCreationForm):
    class Meta:
        model = User

        phone = PhoneNumberField(region='KR')

        fields = ['username', 'password1', 'password2', 'phone']