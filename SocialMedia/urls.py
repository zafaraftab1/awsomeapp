from django.urls import path,include
from SocialMedia import views

urlpatterns = [
path('home/', views.home, name='home'),
]