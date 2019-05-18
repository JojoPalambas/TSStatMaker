from django.shortcuts import render
from django.shortcuts import HttpResponse
from db import init as init_db


def index(request):
    context = {}
    return render(request, 'StatViz/dashboard.html', context)


def init(request):
    context = {}
    init_db.reset()
    return HttpResponse("Init completed!")