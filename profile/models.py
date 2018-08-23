from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tel = models.CharField(max_length=255, blank=True)
    desc = models.CharField(max_length=255, blank=True)

    @property
    def username(self):
        return self.user.username
