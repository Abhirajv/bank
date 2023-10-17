from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Bank



# Create your views here.
def demo(request):
    return render(request,"index.html")

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('newlog')
        else:
            messages.info(request,"invalid password")
            return redirect('login')

    return render(request,"login.html")


def register(request):
    if request.method== 'POST':
        username=request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save();
                return redirect('login')

        else:
            messages.info(request,"username taken")
        return redirect('register')


    return render(request,"register.html")



def form(request):


    return render(request,"form.html")


def message(request):
    return render(request,"message.html")

def newlog(request):
    return render(request,"newlog.html")


def logout(request):
    auth.logout(request)
    return redirect('login')

def index(request):
    return render(request,"index.html")