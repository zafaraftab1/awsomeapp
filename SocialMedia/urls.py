from django.urls import path,include
from SocialMedia import views
from SocialMedia.views import *

urlpatterns = [
    path('home/', views.home, name='home'),
    path('category/<tag>/',views.home,name='category-view'),
    path('post/create/',views.postCreated,name='post-create'),
    path('post/delete/<pk>/',views.postDelete,name='post-delete'),
    path('post/edit/<pk>/',views.postEdit,name='post-Edit'),
    path('post/<pk>/',views.postPageView,name='post-Page'),

]