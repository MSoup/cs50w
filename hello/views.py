from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "hello/index.html")

def dave(request):
    return HttpResponse("Hello Dave")

def greet(request, name: str):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })
