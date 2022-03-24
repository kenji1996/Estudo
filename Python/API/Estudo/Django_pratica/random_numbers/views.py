from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
def index(request, lista):
    return render(request, "templates/random.html", {
        "lista": lista
    })