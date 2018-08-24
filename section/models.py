from django.db import models


class Section(models.Model):
    name = models.CharField(max_length=255)
    creator = models.CharField(max_length=255)
    created_time = models.DateTimeField(auto_now_add=True)
