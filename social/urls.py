from django.conf.urls import url
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from .import views

from django.conf import settings
from django.views.static import serve


urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^google_home/$', views.googleauth, name='googleauth'),
    url(r'^home/$', views.socialgoogle, name='socialgoogle'),
    url(r'^facebook_home/$', views.facebookauth, name='facebookauth'),
    url(r'^redirect/$', views.userauthenticate, name='userauthenticate'),
    url(r'^social_facebook/$', views.socialfacebook, name='socialfacebook'),
    url(r'^logout/$', views.userlogout, name='userlogout'),
    url(r'^login/$', views.userlogin, name='userlogin'),
]
