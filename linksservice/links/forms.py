from django import forms
from .models import Link

class CreateLink(forms.ModelForm):
    full_link = forms.URLField(max_length=200, label='Полная ссылка:', widget=forms.TextInput(attrs={'class': 'form-field', 'placeholder': 'Введите полную ссылку'}))
    nickname = forms.CharField(max_length=20, label='Сокращение:', widget=forms.TextInput(attrs={'class': 'form-field', 'placeholder': 'Введите сокращение'}))


    class Meta:
        model = Link
        fields = ['full_link', 'nickname']