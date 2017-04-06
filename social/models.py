from __future__ import unicode_literals

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
import datetime


class FacebookUser(models.Model):
    facebook_user = models.ForeignKey(User, blank=True, null=True)
    facebook_userid = models.CharField(max_length=200)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.facebook_user

class GoogleUser(models.Model):
    google_user = models.ForeignKey(User, blank=True, null=True)
    google_userid = models.CharField(max_length=200)
    name = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)

    def __int__(self):
        return self.google_user
