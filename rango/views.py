from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Working! <br><a href='/rango/about/'>About</a>")
    
def about(request):
    return HttpResponse("<a href='/rango/'>Index</a>")
