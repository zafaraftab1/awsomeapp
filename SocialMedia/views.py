from django.shortcuts import render

from SocialMedia.models import *


# Create your views here.
def home(request):
    posts=Post_models.objects.all()

    for post in posts:
        print(post.image.url)  # If using ImageField
    return render(request, 'myHome/home.html', {'posts': posts})
    #return render(request, 'myHome/home.html', {'posts':posts})