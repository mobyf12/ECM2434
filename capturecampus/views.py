from ast import Global
from dataclasses import fields
from pprint import pprint
from re import X, template
from sys import flags
from unicodedata import name
from urllib import request
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import *
from django.views.generic.edit import CreateView , UpdateView
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import *

import json

def get_player():
    pass



def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("/playercreation/")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})




def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect(landing_page_request)

def home(request,username):

    
    player = Player.objects.get(name = (User.objects.get(username = username)))
    flag = Flag.objects.all()
    return render(request, "home.html",{'Player': player, 'Flag':flag})


def queens(request):
    flag = Flag.objects.all()
    
    return render(request, "queens.html")
def into(request):
    flag = Flag.objects.all()
    return render(request, template_name= "into.html")

def sport(request):
    flag = Flag.objects.all()
    return render(request, template_name= "sport.html")
def amory(request):
    flag = Flag.objects.all()
    return render(request, template_name= "amoury.html")
def east(request):
    flag = Flag.objects.all()
    return render(request, template_name= "east.html")
def buisness(request):
    flag = Flag.objects.all()
    return render(request, template_name= "buisness.html")
def rowe(request):
    flag = Flag.objects.all()
    return render(request, template_name= "rowe.html")
def washington(request):
    flag = Flag.objects.all()
    return render(request, template_name= "washington.html")
def forum(request):
    flag = Flag.objects.all()
    return render(request, template_name= "forum.html")
def landing_page_request(request):
    return render(request, template_name= "landingpage.html")
def about(request):
    return render(request, template_name= "about.html")

def teamcreate_request(request):
    if request.method == "POST":
        form = NewTeamForm(request.POST)
        if form.is_valid():
            team = form.save()
            messages.success(request, "Team creation successful.")
            return redirect(landing_page_request)
        messages.error(request, "Unsuccessful creation. Invalid information.")
    form = NewTeamForm()
    return render(request, "teamcreation.html", context={"form":form})

def playercreate_request(request):
    if request.method == "POST":
        form = NewPlayerForm(request.POST)
        if form.is_valid():
            global player 
            player = form.save()
            messages.success(request, "Player creation successful.")
            return redirect("/home/%s" % player)
        messages.error(request, "Unsuccessful creation. Invalid information.")
    form = NewPlayerForm()
    return render(request, "playercreation.html", context={"form":form})

def flagcreate_request(request):
    if request.method == "POST":
        form = NewFlagForm(request.POST)
        if form.is_valid():
            flag = form.save()
            
            return redirect(landing_page_request)
        messages.error(request, "Unsuccessful creation. Invalid information.")
    form = NewFlagForm()
    return render(request, "flagcreation.html", context={"form":form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
    
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("/home/%s" % username)
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})

def capture_flag(request):
    if request.method == "POST":
        form = FlagForm(request.POST)
        if form.is_valid():
            y = form.cleaned_data.get("flag")
            x = form.cleaned_data.get("name")
            z = form.cleaned_data.get("code")
            player = Player.objects.get(name = (User.objects.get(username = x)))
            if z == y.get_code():
                player.captured_flag(y.get_score())
                y.delete()
                return redirect("/home/%s" % x)
            else:
                messages.error(request, "Invalid code")
                return redirect("/capture_flag/")

    form = FlagForm()
   
    return render(request, "capture_flag.html", context={"form":form})

