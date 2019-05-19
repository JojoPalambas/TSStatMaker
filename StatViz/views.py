from django.shortcuts import render
from django.shortcuts import HttpResponse
from db import init as init_db

from StatViz.models import Task


def init(request):
    context = {}
    init_db.reset()
    return HttpResponse("Init completed!")


def index(request):
    context = {}
    return render(request, 'StatViz/dashboard.html', context)


def line_per_project(request):
    tasks = Task.objects.all()
    projects = []
    # Building the projects list with their names and 
    for task in tasks:
        placed = False
        for fp in projects:
            if fp["name"] == task.project_name:
                placed = True
                fp["tasks"].append(task)
                continue
        if not placed:
            projects.append({"name": task.project_name, "tasks": [task]})

    context = {
        "projects": projects
    }
    return render(request, 'StatViz/line_per_project.html', context)
