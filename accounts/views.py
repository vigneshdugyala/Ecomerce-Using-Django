from django.shortcuts import render, redirect
from django.contrib.auth.models import auth,User
from django.contrib import messages
from django.core.cache import cache
# Create your views here.
user=None
def register(request):
    if request.method=="POST":
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        username=request.POST["username"]
        email=request.POST["email"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]
        if User.objects.filter(username=username).exists():
            messages.info(request,'Username Taken')
            return redirect(register)
        elif User.objects.filter(email=email).exists():
             messages.info(request,'Email Taken')
             return redirect(register)
        elif password1 != password2:
             messages.info(request,'Password missmatch')
             return redirect(register)
        else:
            user=User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
            user.save()
            messages.info(request,'Registered Succesfully !')
            return redirect('login')


    return render(request,"reg.html")
def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            request.session['user_id']=user.id
            return redirect('/')
        else:
            messages.info(request,'Username or Password is incorrect !')
            return redirect('login') 

    return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return redirect('/')