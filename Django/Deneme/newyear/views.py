from django.shortcuts import render
import requests
import datetime

# Create your views here.

def index(request):
    now = datetime.datetime.now()
    return render(request, "newyear/index.html" , {"newyear": now.month == 8 and now.day == 7})