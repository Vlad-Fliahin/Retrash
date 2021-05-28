from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    data = {
    	'title': 'Main page',
    	'values': ['Some', 'Hello', 123]
   	}
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')


def stats(request):
    return HttpResponse("<h4>Stats</h4>")