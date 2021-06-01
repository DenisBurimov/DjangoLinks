from django import forms
from .models import Link

class CreateLink(forms.ModelForm):
    full_link = forms.URLField(max_length=200)
    nickname = forms.CharField(max_length=20)
    short_link = forms.CharField(max_length=20)


    class Meta:
        model = Link
        fields = ['full_link', 'nickname', 'short_link']