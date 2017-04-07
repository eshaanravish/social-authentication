from django.conf.urls import url
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from .import views

from django.conf import settings
from django.views.static import serve


urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^google_home/$', views.googleauth, name='googleauth'),
    url(r'^email_request/$', views.get_email, name='get_email'),
    url(r'^linkedin_email_request/$', views.get_linkedin_user_email, name='get_linkedin_user_email'),
    url(r'^linkedin_home/$', views.linkedinauth, name='linkedinauth'),
    url(r'^linkedin/$', views.get_linkedin_auth, name='get_linkedin_auth'),
    url(r'^instagram_home/$', views.instaauth, name='instaauth'),
    url(r'^main/$', views.get_insta_auth, name='get_insta_auth'),
    url(r'^home/$', views.socialgoogle, name='socialgoogle'),
    url(r'^facebook_home/$', views.facebookauth, name='facebookauth'),
    url(r'^redirect/$', views.userauthenticate, name='userauthenticate'),
    url(r'^social_facebook/$', views.socialfacebook, name='socialfacebook'),
    url(r'^logout/$', views.userlogout, name='userlogout'),
    url(r'^login/$', views.userlogin, name='userlogin'),
]
