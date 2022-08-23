from django import forms
from .models import User


class LoginForm(forms.Form):
    email = forms.CharField(label='', max_length=200, widget=forms.EmailInput(attrs={'placeholder': 'ایمیل خود را وارد کنید...'}))
    password = forms.CharField(max_length=200, widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور خود را وارد کنید..'}))
