from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'numbum/home.html')


def rooms(request):
    return HttpResponse("<h1>Rooms</h1>")
