from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from .models import Patron, Favorite
from django.contrib import messages
from django.db import connection

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

@login_required
def update_profile(request):
    if request.method == "POST":
        new_bio = request.POST.get('bio')
        # Get the patron object for the logged-in user
        patron = request.user.patron
        patron.bio = new_bio
        patron.save() # This updates the record in Supabase
        messages.success(request, "Bio updated successfully!")
        return redirect('user')
    return redirect('user')

@login_required
def delete_account(request):
    if request.method == "POST":
        user_id = request.user.id
        
        # 1. End the session in the browser first
        logout(request)
        
        # 2. Direct strike to the database
        # This bypasses all internal Django checks for missing tables
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM auth_user WHERE id = %s", [user_id])
            
        messages.success(request, "Your Patron record has been purged from the Vault.")
        return redirect('onboarding')
        
    return redirect('user')


def logout_view(request):
    logout(request)
    return redirect('onboarding')

@login_required
def user(request):
    # 1. Safety check for Patron profile
    try:
        patron = request.user.patron
    except Exception:
        Patron.objects.create(user=request.user)
    
    # 2. Fetch all favorites for this user
    favorites = Favorite.objects.filter(user=request.user)
    
    # 3. Pass everything to the template
    return render(request, "user.html", {'favorites': favorites})

@login_required
def toggle_favorite(request):
    if request.method == "POST":
        artwork = request.POST.get('artwork_name')
        img = request.POST.get('image_url')
        page = request.POST.get('page_url')
        
        fav, created = Favorite.objects.get_or_create(
            user=request.user, 
            artwork_name=artwork,
            defaults={'image_url': img, 'page_url': page}
        )
        
        if not created:
            fav.delete() # Unfavorite if it already exists
            
        return redirect(page) # Return to the artist page
    return redirect('home')
