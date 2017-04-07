from django.core.mail import send_mail
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import FacebookUser, GoogleUser, LinkedinUser, InstagramUser

class SignUpForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder':'Username'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder':'EmailId'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder':'Password'})

class EmailForm(ModelForm):

    class Meta:
        model = FacebookUser
        fields = ('facebook_userid', 'name', 'email')

    def __init__(self, *args, **kwargs):
        super(EmailForm, self).__init__(*args, **kwargs)
        self.fields['facebook_userid'].widget.attrs.update({'class': 'form-control'})
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder':'EmailId'})

class LinkedinEmailForm(ModelForm):

    class Meta:
        model = LinkedinUser
        fields = ('linkedin_userid', 'name', 'email')

    def __init__(self, *args, **kwargs):
        super(LinkedinEmailForm, self).__init__(*args, **kwargs)
        self.fields['linkedin_userid'].widget.attrs.update({'class': 'form-control'})
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder':'EmailId'})
