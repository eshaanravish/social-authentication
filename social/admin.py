from django.contrib import admin

# Register your models here.
from .models import FacebookUser, GoogleUser



class FacebookUserAdmin(admin.ModelAdmin):
    list_display = ('facebook_user', 'facebook_userid', 'email')

admin.site.register(FacebookUser, FacebookUserAdmin)

class GoogleUserAdmin(admin.ModelAdmin):
    list_display = ('google_user', 'google_userid', 'email')

admin.site.register(GoogleUser, GoogleUserAdmin)
