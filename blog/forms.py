from django.http import HttpResponse
from django import forms
from .models import post


class PostForm(forms.ModelForm):
    class Meta:
        model = post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
