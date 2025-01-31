from django.forms import ModelForm
from django import forms
from .models import *

class PostCreateForm(ModelForm):
    class Meta:
        model = Post_models
        fields = '__all__'
        labels = {
            'body': 'Captions',
            'tags' : 'Category'
        }
        widgets = {
            'body': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Add a caption ...',
                'class': 'font1 text-4xl',
            }),
            'tags': forms.CheckboxSelectMultiple(),
        }

class PostEditForm(ModelForm):
    class Meta:
        model = Post_models
        fields = ['title','body', 'tags']
        labels = {
            'body': '',
            'tags': 'category',
        }
        widgets = {
            'body': forms.Textarea(attrs={'rows': 3, 'class': 'font1 text-4xl'}),
            'tags': forms.CheckboxSelectMultiple(),
        }