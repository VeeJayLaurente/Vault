from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from .models import Patron
from django.contrib import messages
from django.http import HttpResponse

def onboarding(request):
    return render(request,"onboarding.html")

def home(request):
    return render(request,"home.html")

def login(request):
    if request.method == "POST":
        username_field = request.POST.get('username') # We'll use username as the login key
        password_field = request.POST.get('password')
        
        user = authenticate(request, username=username_field, password=password_field)
        
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')
    return render(request,"login.html")

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return redirect('register')

        # Create User and Profile
        user = User.objects.create_user(username=username, first_name=fname, last_name=lname, email=email, password=password)
        Patron.objects.create(user=user)
        
        messages.success(request, "Registration successful! Please login.")
        return redirect('login')
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
    # Only show if logged in
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request,"user.html")