"""Mainproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from . import views

urlpatterns = [
    path('',views.Index,name='Index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('chinese/', views.chinese, name='chinese'),
    path('italian/', views.italian, name='italian'),
    path('indian/', views.indian, name='indian'),
    path('maindishes/', views.maindishes, name='maindishes'),
    path('login/', views.login, name='login'),
    path('signup/',views.signup,name='signup'),
    path('soup/', views.soup, name='soup'),
    path('salads/',views.salads,name='salads'),
    path('appetizers/', views.appetizers, name='appetizers'),
    path('addrecipe/',views.addrecipe,name='addrecipe'),
    path('clientaddrecipe/',views.clientaddrecipe,name='clientaddrecipe'),
    path('maindishes/maindish2/<int:id>',views.maindish2,name='maindish2'),
    path('maindishes/maindish2/comment/<slug:slug>', views.comment, name='comment'),
    path('home/',views.home,name='home'),
    path('userinput',views.home,name='userinput'),



    path('logout/',views.logout,name='logout'),

]
