from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return HttpResponse("Hello, world. You're at the home page.")

def contact(request):
    return HttpResponse("Hello, world. You're at the contact page.")

def blog(request):
    return HttpResponse("Hello, world. You're at the blog page.")
