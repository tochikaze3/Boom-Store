from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Account


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ('email',)

class CustomUserChangeForm(UserChangeForm):
    email =forms.EmailField(max_length=200)
    
    class Meta:
        model = User
        fields = ('email',)