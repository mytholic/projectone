"""startup3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pizza.views import logins,welcome,auth,logouts,count,delete,homepage,customersignin,userlogin,authenticateuser,welcomeuser,logoutuser,placeorder
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/',logins),
    path('auth/',auth),
    path('welcome/',welcome),
    path('logout/',logouts),
    path('add/',count),
    path('delete/<int:pizzaid>/',delete),
    path('',homepage),
    path('customer/',customersignin),
    path('userlogin/',userlogin,name='userlogin'),
    path('userverification/',authenticateuser),
    path('welcomeuser/',welcomeuser,name="wel"),
    path('logoutuser/',logoutuser),
    path('placed/',placeorder)

    

]

urlpatterns+=staticfiles_urlpatterns()