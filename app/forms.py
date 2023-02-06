from django import forms
from django.urls import reverse_lazy

from .models import SobunPost


class SobunPostForm(forms.ModelForm):
    class Meta:
        model = SobunPost
        exclude = ['is_deleted', 'user', 'area']


