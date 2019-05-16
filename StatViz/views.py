from django.shortcuts import render
from django.shortcuts import HttpResponse
from db import reset


def index(request):
    context = {}
    return render(request, 'StatViz/dashboard.html', context)


def init(request):
    context = {}
    reset.init()
    return HttpResponse("Init completed!")