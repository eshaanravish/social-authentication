from __future__ import unicode_literals

import datetime
from django.utils import timezone
# Create your models here.
from django.contrib.auth.models import User
from django.db import models


class LinkedinUser(models.Model):
    linkedin_user = models.ForeignKey(User, blank=True, null=True)
    linkedin_userid = models.CharField(max_length=200)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.linkedin_userid


class InstagramUser(models.Model):
    instagram_user = models.ForeignKey(User, blank=True, null=True)
    instagram_userid = models.CharField(max_length=200)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.instagram_user


class FacebookUser(models.Model):
    facebook_user = models.ForeignKey(User, blank=True, null=True)
    facebook_userid = models.CharField(max_length=200)
    name = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.facebook_userid

class GoogleUser(models.Model):
    google_user = models.ForeignKey(User, blank=True, null=True)
    google_userid = models.CharField(max_length=200)
    name = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)

    def __int__(self):
        return self.google_user

class TwitterProfile(models.Model):
    user = models.ForeignKey(User)
    oauth_token = models.CharField(max_length=200)
    oauth_secret = models.CharField(max_length=200)

    def __int__(self):
        return self.user
