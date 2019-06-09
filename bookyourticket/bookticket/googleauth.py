from django.conf import settings
from django.http import HttpResponse
import requests
from django.contrib.auth import authenticate, login, logout
from bookticket.models import OwnUser
from django.shortcuts import render, redirect
def google_auth_view(request):
    token_request_uri = "https://accounts.google.com/o/oauth2/auth"
    response_type = "code"
    client_id = settings.ID
    redirect_uri = "http://localhost:8000/oauth2redirect/"
    scope = "https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email"
    url = f"{token_request_uri}?response_type={response_type}&client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}"
    resp = requests.get(url)
    return HttpResponse(resp.text)
def redirect_view(request,*args, **kwargs):
    code=request.GET.get('code')
    access_token_uri = 'https://accounts.google.com/o/oauth2/token'
    redirect_uri = "http://localhost:8000/oauth2redirect/"
    resp = requests.post(access_token_uri, json={
        'code':code,
        'redirect_uri':redirect_uri,
        'client_id':settings.ID,
        'client_secret':settings.SECRET,
        'grant_type':'authorization_code'
    })
    token_data = resp.json().get("access_token")
    resp = requests.get(f"https://www.googleapis.com/oauth2/v1/userinfo?access_token={token_data}")
    user_data = resp.json()
    username = user_data.get("email")
    user = OwnUser.objects.filter(username=username)
    if user:
        user = user[0]
    else:
        user = OwnUser.objects.create_user(username=username,password="1234WERTT")
    login(request, user)
    #this gets the google profile!!
    return redirect("/bookticket/index")