from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, "logreg_app/index.html")

def registration(request):
    errors = User.objects.basic_validator(request.POST)
    request.session['email'] = request.POST['email']
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags='register')
        return redirect('/')
    else:
        password = request.POST['password']
        hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        
        new_user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], dob=request.POST['dob'], email=request.POST['email'], password=hashed_pw)
        new_user.save()

        return redirect('/success')
    

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags='login')
        return redirect('/')
    else: 
        user_from_db = User.objects.get(email=request.POST['email_login'])
        logged_user = user_from_db
        if bcrypt.checkpw(request.POST['password_login'].encode(), logged_user.password.encode()):
            request.session['email'] = logged_user.email
            return redirect('/success')
        else:
            return redirect('/')

def success(request):
    if "email" not in request.session:
        return redirect('/')
    else:
        context = {
            "this_user": User.objects.get(email=request.session['email'])
        }
        return render(request, "logreg_app/welcome.html", context)

def logout(request):
    request.session.clear()
    return redirect('/')
