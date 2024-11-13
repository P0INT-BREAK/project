from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def projects(request):
    return render(request, 'projects.html', )