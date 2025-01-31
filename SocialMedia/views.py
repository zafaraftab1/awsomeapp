from unicodedata import category

from django.forms import ModelForm, forms
from django.shortcuts import render,redirect,get_object_or_404
from django import forms
from SocialMedia.models import *
from django.forms import ModelForm
from django.contrib import messages
from .forms import *

# Create your views here.

#def home(request):
    #posts=Post_models.objects.all()
    #return render(request, 'myHome/home.html', {'posts': posts})

#def category_view(request,tag):
    #posts=Post_models.objects.filter(tags__slug=tag)
    #return render(request, 'myHome/home.html', {'posts': posts})

def home(request,tag=None):
    if tag:
        posts=Post_models.objects.filter(tags__slug=tag)
        tag= get_object_or_404(Tags,slug=tag)
    else:
        posts=Post_models.objects.all()
    categories= Tags.objects.all()

    context={
        'posts':posts,
        'categories':categories,
        'tag':tag,
    }
    return render(request, 'myHome/home.html', context)


def postCreated(request):
    form = PostCreateForm()
    if request.method == 'POST':
        form = PostCreateForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect('home')
    return render(request, 'layout/created_post.html', {'form': form})

def postDelete(request,pk):
    post=get_object_or_404(Post_models,id=pk)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted successfully')
        return redirect('home')
    return render(request, 'layout/post_delete.html',{'post': post})
    #post = Post_models.objects.get(pk=pk)

def postEdit(request,pk):
    post=get_object_or_404(Post_models,id=pk)
    form = PostEditForm(instance=post)
    if request.method == 'POST':
        form = PostEditForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post edited successfully')
            return redirect('home')
    context = {
        'form': form,
        'post': post,
    }
    return render(request, 'layout/post_edit.html', context)

def postPageView(request,pk):
    #post = Post_models.objects.get(id=pk)
    post=get_object_or_404(Post_models,id=pk)
    return render (request,'layout/post_page.html', {'post': post})

