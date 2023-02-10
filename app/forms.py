from django import forms
from django.urls import reverse_lazy

from .models import SobunPost, Sobun, SobunRate


class SobunPostForm(forms.ModelForm):
    class Meta:
        model = SobunPost
        exclude = ['is_deleted', 'user', 'area', 'tags']


class SobunForm(forms.ModelForm):
    class Meta:
        model = Sobun
        fields = ('time', 'status',)

class SobunRateForm(forms.ModelForm):
    class Meta:
        model = SobunRate
        fields = ('type', 'detail',)