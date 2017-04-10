from django.contrib import admin

# Register your models here.
from .models import FacebookUser, GoogleUser, LinkedinUser, InstagramUser, TwitterProfile



class LinkedinUserAdmin(admin.ModelAdmin):
    list_display = ('linkedin_user', 'linkedin_userid', 'email')

admin.site.register(LinkedinUser, LinkedinUserAdmin)

class InstagramUserAdmin(admin.ModelAdmin):
    list_display = ('instagram_user', 'instagram_userid', 'email')

admin.site.register(InstagramUser, InstagramUserAdmin)

class FacebookUserAdmin(admin.ModelAdmin):
    list_display = ('facebook_user', 'facebook_userid', 'email')

admin.site.register(FacebookUser, FacebookUserAdmin)

class GoogleUserAdmin(admin.ModelAdmin):
    list_display = ('google_user', 'google_userid', 'email')

admin.site.register(GoogleUser, GoogleUserAdmin)

class TwitterProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'oauth_token')

admin.site.register(TwitterProfile, TwitterProfileAdmin)
