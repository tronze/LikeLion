from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.localtime)


class Comment(Post):
    title = None
    parent = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='parent_post')
