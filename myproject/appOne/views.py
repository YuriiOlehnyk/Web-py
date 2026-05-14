from urllib import request
from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.


def index(request):
    ip = request.META.get('REMOTE_ADDR')
    return render(request, 'appOne/index.html', {'ip': ip})

def connection_check(request):
    return HttpResponse('<h1>Hello, connection established successfully!</h1>')