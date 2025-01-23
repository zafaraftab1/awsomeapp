from django.contrib import admin

import SocialMedia
from .models import *

# Register your models here.
admin.site.register(Post_models)


def site(request):
    return None