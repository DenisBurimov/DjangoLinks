from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-field', 'placeholder': 'Введите имя пользователя'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-field', 'placeholder': 'Введите email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-field', 'placeholder': 'Введите пароль'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields['password2']

class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-field'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-field'}))

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']