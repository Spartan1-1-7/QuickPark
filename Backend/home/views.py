# home/views.py
from django.shortcuts import render
from django.template.context_processors import request


def landing_page(request):
    return render(request, 'landing_page.html')

def login_selection(request):
    return render(request, 'login_selection.html')

def user_login(request):
    return render(request,'user_login.html')

def admin_registration(request):
    return render(request,'admin_registration.html')

def admin_management(request):
    return render(request,'admin_management.html')

def feedback(request):
    return render(request,'feedback.html')

def nearby_parking(request):
    return render(request,'nearby_parking.html')

def container(request):
    return render(request,'Container.html')