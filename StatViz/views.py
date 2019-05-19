from django.shortcuts import render
from django.shortcuts import HttpResponse
from db import init as init_db
import datetime

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

    # Building the list of the projects names
    for task in tasks:
        placed = False
        for project in projects:
            if project == task.project_name:
                placed = True
                continue
        if not placed:
            projects.append(task.project_name)

    # Building as an histogram all the dates

    # Fake data to be sent
    dated_tasks = [
        [datetime.date(2019, 5, 13), "240", "60", "0"],
        [datetime.date(2019, 5, 14), "350", "75", "0"],
        [datetime.date(2019, 5, 15), "400", "0", "0"],
        [datetime.date(2019, 5, 16), "380", "40", "180"],
        [datetime.date(2019, 5, 17), "120", "120", "60"],
        [datetime.date(2019, 5, 18), "0", "60", "120"],
        [datetime.date(2019, 5, 19), "60", "60", "60"],
    ]
    projects = ["EPITA", "RIX", "Petits jeux & programmes"]

    context = {
        "projects": projects,
        "dated_tasks": dated_tasks
    }
    return render(request, 'StatViz/line_per_project.html', context)
