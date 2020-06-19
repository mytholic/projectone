from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import PIZZA,customer,order
from django.contrib.auth.models import User
# Create your views here.
def logins(request):
    return render(request,'login.html')

def auth(request):

    username=request.POST['username']
    password=request.POST['password']

    user= authenticate(username=username,password=password)
    if user is not None:
        login(request,user)
        return render(request,'welcome.html',{'username':username})
    if user is None:
        messages.add_message(request,messages.ERROR,"INCORRECT USERNAME OR PASSWORD")
        return redirect('/')
def welcome(request):
    context={'pizzast':PIZZA.objects.all()}
    return render(request,'welcome.html',context)

def logouts(request):
    logout(request)
    return render(request,'login.html')

def count(request):
    pizza=request.POST['pizza']
    price=request.POST['price']
    PIZZA(pizza=pizza,price=price).save()
    return redirect('/welcome')

def delete(request,pizzaid):
    PIZZA.objects.filter(id=pizzaid).delete()
    return redirect('/welcome')

def homepage(request):
    return render(request,'homepage.html')

def customersignin(request):
    username=request.POST['username']
    password=request.POST['password']
    email=request.POST['email']
    if User.objects.filter(username=username).exists():
        messages.add_message(request,messages.ERROR,"user already exist")
        return redirect('/')
    User.objects.create_user(username=username,password=password).save()
    lastobject=len(User.objects.all())-1
    customer(userid=User.objects.all()[int(lastobject)].id,email=email).save()
    messages.add_message(request,messages.ERROR,"user signed in")
    return redirect('/')
def userlogin(request):
    return render(request,'userlogin.html')

def authenticateuser(request):
    username=request.POST['username']
    password=request.POST['password']

    user= authenticate(username=username,password=password)
    if user is not None:
        login(request,user)
        return render(request,'welcomeuser.html',{'username':username,'pizza':PIZZA.objects.all()})
    if user is None:
        messages.add_message(request,messages.ERROR,"INCORRECT USERNAME OR PASSWORD")
        return render(request,'userlogin.html')

def welcomeuser(request):
    return render(request,'welcomeuser.html',)

def logoutuser(request):
    logout(request)
    return redirect('userlogin')

def placeorder(request):

    username=request.user.username
    address=request.POST['address']
    messages.add_message(request,messages.ERROR,"order place successfully")
    order(username=username,address=address)
    return redirect("wel")