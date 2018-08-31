from django.db import models
from django.contrib.auth.models import User


class Collection(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    abstract = models.CharField(max_length=100, blank=True)
    thumb = models.URLField(blank=False)
    context = models.URLField(blank=False)
