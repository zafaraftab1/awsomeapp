from django.shortcuts import render


# Create your views here.
def home(request):
    title='Welcome to My Social Media App'
    return render(request, 'start_template/base.html', {'title1':title})