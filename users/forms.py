from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import User


class UserSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'username', 'password1', 'password2')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'input100', 'placeholder': 'First name'}),
            'last_name': forms.TextInput(attrs={'class': 'input100', 'placeholder': 'Last name'}),
            'email': forms.EmailInput(attrs={'class': 'input100', 'placeholder': 'Email'}),
            'phone_number': forms.TextInput(attrs={'class': 'input100', 'placeholder': 'Phone number'}),
            'username': forms.TextInput(attrs={'class': 'input100', 'placeholder': 'Username'}),
            'password1': forms.PasswordInput(attrs={'class': 'input100', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'input100', 'placeholder': 'Repeat password'}),

        }


class UserSigninForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'placeholder': 'Username kiriting'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input100', 'placeholder': 'Parolni kiriting'}))
