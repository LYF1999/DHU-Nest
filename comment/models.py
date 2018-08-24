from django.db import models
from django.contrib.auth.models import User
from post.models import Post


# Create your models here.

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    reply = models.ForeignKey('self', on_delete=models.SET_NULL, null=True)

