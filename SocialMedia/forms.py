from django.forms import ModelForm
from django import forms
from .models import *

class PostCreateForm(ModelForm):
    class Meta:
        model = Post_models
        fields = '__all__'
        labels = {
            'body': 'Captions',  # Correctly label the 'body' field
        }
        widgets = {
            'body': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Add a caption ...',
                'class': 'font1 text-4xl',
            }),
        }