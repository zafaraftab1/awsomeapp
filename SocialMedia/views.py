from django.forms import ModelForm, forms
from django.shortcuts import render,redirect
from django import forms
from SocialMedia.models import *
from django.forms import ModelForm
from django.contrib import messages
from .forms import *

# Create your views here.
def home(request):
    posts=Post_models.objects.all()
    return render(request, 'myHome/home.html', {'posts': posts})

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

def postCreated(request):
    form = PostCreateForm()
    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect('home')
    return render(request, 'layout/created_post.html', {'form': form})

def postDelete(request,pk):
    post = Post_models.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted successfully')
        return redirect('home')
    return render(request, 'layout/post_delete.html',{'post': post})
    #post = Post_models.objects.get(pk=pk)

def postEdit(request,pk):
    post = Post_models.objects.get(id=pk)
    return render(request, 'layout/post_edit.html', {'post': post})