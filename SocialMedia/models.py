import uuid

from django.db import models

# Create your models here.
class Post_models(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    image = models.ImageField(upload_to='SocialMediaCategory/')
    created = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=120,default=uuid.uuid4,editable=False,unique=True,primary_key=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']