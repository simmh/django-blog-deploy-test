from django import forms
from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['category', 'title', 'body']
        widgets = {
            'category': forms.Select(attrs={'class': 'uk-select'}),
            'title': forms.TextInput(attrs={'class': 'uk-input'}),
            'body': forms.Textarea(attrs={'class': 'uk-textarea'}),
        }
