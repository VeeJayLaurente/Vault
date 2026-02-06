from django.shortcuts import render
from django.http import HttpResponse

def onboarding(request):
    return render(request,"onboarding.html")

def home(request):
    return render(request,"home.html")

def login(request):
    return render(request,"login.html")

def register(request):
    return render(request,"register.html")

def monet(request):
    return render(request,"monet.html")

def gogh(request):
    return render(request,"gogh.html")

def picasso(request):
    return render(request,"picasso.html")

def dali(request):
    return render(request,"dali.html")

def user(request):
    return render(request,"user.html")