from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Invitation


class InvitationForm(ModelForm):
    class Meta:
        model = Invitation
        exclude = ("from_user", "timestamp")


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=300, required=False)
    last_name = forms.CharField(max_length=300, required=False)
    email = forms.EmailField(max_length=50)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')