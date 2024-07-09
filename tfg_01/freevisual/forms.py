from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    specialties = forms.CharField(widget=forms.Textarea)  # Campo de especialidades

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'specialties']
