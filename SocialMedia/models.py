import uuid

from django.db import models

# Create your models here.
class Post_models(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    image = models.ImageField(upload_to='SocialMediaCategory/')
    tags = models.ManyToManyField('Tags')
    created = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=120,default=uuid.uuid4,editable=False,unique=True,primary_key=True)

    def __str__(self):
        return self.title

    class Meta:
       ordering = ['-created']

class Tags(models.Model):
    name = models.CharField(max_length=120)
    image=models.FileField(upload_to='icon/',null=True, blank=True,default='icon/default-icon.png')
    slug = models.SlugField(max_length=120, unique=True)
    order =models.IntegerField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']