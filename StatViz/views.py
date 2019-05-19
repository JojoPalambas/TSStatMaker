from django.shortcuts import render
from django.shortcuts import HttpResponse
from db import init as init_db


def init(request):
    context = {}
    init_db.reset()
    return HttpResponse("Init completed!")


def index(request):
    context = {}
    return render(request, 'StatViz/dashboard.html', context)


def line_per_project(request):
    context = {}
    return render(request, 'StatViz/line_per_project.html', context)
