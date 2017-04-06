import json
import datetime
# import httplib2
import urllib2
import requests

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect

from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from social.models import FacebookUser, GoogleUser

from social.forms import SignUpForm

import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

def userlogin(request):
    if request.user.is_authenticated():
        return render(request, 'social/dashboard.html')
    else:
        if request.method == "POST":
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            if username and password:
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return render(request, 'social/dashboard.html')
                else:
                    error_message = "You have provided invalid credentials."
            else:
                error_message = "All fields are mandatory."
        else:
            error_message = ""
        return render(request, 'social/home.html', {'error_message': error_message})


def homepage(request):
    # if request.user.is_authenticated():
    #     return render(request, 'social/dashboard.html')
    # else:
    if request.method == "POST":
        form = SignUpForm(request.POST, use_required_attribute= False)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            new_user.save()
            return render(request, 'social/dashboard.html')
        else:
            error_message = "Please fill the valid details."
            return render(request, 'social/home.html', {'form': form, 'error_message': error_message})
    else:
        error_message = ""
        form = SignUpForm(request.POST, use_required_attribute= False)
        return render(request, 'social/home.html', {'form': form, 'error_message': error_message})

def googleauth(request):
    url = "https://accounts.google.com/o/oauth2/auth?scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email&access_type=offline&include_granted_scopes=true&state=state_parameter_passthrough_value&redirect_uri=http%3A%2F%2Flocalhost%3A8001%2Fhome&response_type=code&client_id=459600573348-f8ng5ifjugc14t8afnhhcphjml8nckir.apps.googleusercontent.com"
    r = requests.get(url)
    print r.status_code
    return redirect(url)


# def get_google_token(code):


def socialgoogle(request):
    code = request.GET.get('code', '')
    url = 'https://accounts.google.com/o/oauth2/token'
    data = {
        'grant_type' : 'authorization_code',
        'redirect_uri' : 'http://localhost:8001/home',
        'client_id' : '459600573348-f8ng5ifjugc14t8afnhhcphjml8nckir.apps.googleusercontent.com',
        'client_secret' : 'NbxNp6yZtN1QiBY-vUQ9zMot',
        'code' : code,
        'scope' : 'https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/gmail.readonly'
    }
    headers = {
        'Host': 'accounts.google.com',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    r = requests.post(url, data= data, headers= headers)
    data = r.json()
    token = data['access_token']
    inspect_token = 'https://www.googleapis.com/oauth2/v1/userinfo?access_token=' + token
    user_data = requests.get(inspect_token)
    data = user_data.json()
    print data
    userid = data['id']
    email = data['email']
    if User.objects.filter(email=email, username=email).exists():
        new_user = User.objects.get(email=email)
        if GoogleUser.objects.filter(google_userid=userid).exists():
            user = User.objects.get(email=email)
            login(request, user)
        else:
            new_googleuser = GoogleUser.objects.create(
                google_user = new_user,
                google_userid = userid,
                email = email,
            )
            new_googleuser.save()
            login(request, new_user)
        message = "logged in successfully."
        return render(request, 'social/dashboard_google.html', {'data': data, 'message': message})
    else:
        new_user = User.objects.create_user(
            username = email,
            email = email,
        )
        new_user.save()
        new_googleuser = GoogleUser.objects.create(
            google_user = new_user,
            google_userid = userid,
            email = email,
        )
        new_googleuser.save()
        login(request, new_user)
        message = "registered successfully."
        return render(request, 'social/dashboard_google.html', {'data': data, 'message': message})

def facebookauth(request):
    url = "https://www.facebook.com/v2.8/dialog/oauth?client_id=237086353424892&redirect_uri=http%3A%2F%2Flocalhost:8001%2Fsocial_facebook&granted_scopes=true&scope=email"
    r = requests.get(url)
    print r.status_code
    return redirect(url)

def socialfacebook(request):
    code = request.GET.get('code', '')
    url = 'https://graph.facebook.com/v2.8/oauth/access_token?client_id=237086353424892&redirect_uri=http%3A%2F%2Flocalhost:8001%2Fsocial_facebook&client_secret=71e32063afaf632812e138a2785591ac&code=' + code
    serialized_data = urllib2.urlopen(url).read()
    data = json.loads(serialized_data)
    token = data['access_token']
    inspect_url = 'https://graph.facebook.com/debug_token?input_token=' + token + '&access_token=237086353424892|IhanNpMQj-dlOkF_Yabj5n8iwA4'
    user_data = urllib2.urlopen(inspect_url).read()
    user_info = json.loads(user_data)
    print user_info
    uid = user_info['data']
    userid = uid['user_id']
    detail_url = 'https://graph.facebook.com/v2.8/' + userid + '?access_token=237086353424892|IhanNpMQj-dlOkF_Yabj5n8iwA4&fields=id,name,about,age_range,birthday,email'
    user_detail = requests.get(detail_url)
    details = user_detail.json()
    print details
    if details['email']:
        email = details['email']
        if User.objects.filter(email=email, username=email).exists():
            new_user = User.objects.get(email=email)
            if FacebookUser.objects.filter(facebook_userid=userid).exists():
                user = User.objects.get(email=email)
                login(request, user)
                message = "logged in successfully."
            else:
                new_facebookuser = FacebookUser.objects.create(
                    facebook_user = new_user,
                    facebook_userid = userid,
                    email = email,
                )
                new_facebookuser.save()
                login(request, user)
        else:
            new_user = User.objects.create_user(
                username = email,
                email = email,
            )
            new_user.save()
            new_facebookuser = FacebookUser.objects.create(
                facebook_user = new_user,
                facebook_userid = userid,
                email = email,
            )
            new_facebookuser.save()
            login(request, new_user)
            message = "registered successfully."
        return render(request, 'social/dashboard_facebook.html', {'details': details, 'message': message})
    else:
        #ask for email in new form field.
        pass
        
def redirecturl(request):
    return render(request, 'social/dashboard.html')

def userauthenticate(request):
    email = request.GET['email']
    if User.objects.filter(username__in = email).count() == 0:
        # do successful login.
        username = email
        password = email
        if username and password:
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/dashboard/')
                pass
            else:
                error_message = "You have provided invalid credentials."
        user = User.objects.get(username__in = email)
        login(request, user)
        return redirect('/')
    else:
        user = User.objects.create_user(
        username= email,
        first_name= first_name,
        last_name= last_name,
        email= email,
        password= email,
        )
        user.save()
        login(request, user)
        return redirect('/dashboard/')
        # return HttpResponse(json.dumps(response))

@login_required(login_url="/login/")
def userlogout(request):
    logout(request)
    return redirect('/')
