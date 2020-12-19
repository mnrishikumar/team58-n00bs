from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup

def home(request):
    return render(request, "emissionnaire/home.html")

def about(request):
    return render(request, "emissionnaire/about.html")

def leaderboard(request):
    return render(request, "emissionnaire/leaderboard.html")
