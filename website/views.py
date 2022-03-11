from django.shortcuts import render
from django.http import HttpResponse

def homescreen(request): 
    return render(request, 'homescreen.html', {})