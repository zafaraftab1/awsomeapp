from django.urls import path,include
from SocialMedia import views
from SocialMedia.views import *

urlpatterns = [
    path('home/', views.home, name='home'),
    path('post/create',views.postCreated,name='post-create')
]