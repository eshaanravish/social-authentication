from django.core.mail import send_mail
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm


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
