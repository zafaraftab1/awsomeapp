from django.shortcuts import render

from SocialMedia.models import *


# Create your views here.
def home(request):
    posts=Post_models.objects.all()
    return render(request, 'myHome/home.html', {'posts': posts})

def postCreated(request):
    return render(request, 'layout/created_post.html')