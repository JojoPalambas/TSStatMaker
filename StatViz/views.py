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


def sub_line_per_project(request, accumulate=False):
    tasks = Task.objects.all()

    # Building the list of the projects names and getting the first and last dates
    projects = ["ALL"]
    first_date = datetime.datetime.now().date()
    last_date = datetime.date(1970, 1, 1)
    for task in tasks:
        # Project-listing part
        placed = False
        for project in projects:
            if project == task.project_name:
                placed = True
                continue
        if not placed:
            projects.append(task.project_name)

        # Date extremums part
        if task.start_date < first_date:
            first_date = task.start_date
        if task.start_date > last_date:
            last_date = task.start_date

    # Building as an histogram all the dates
    histogram = []
    current_date = first_date
    while current_date <= last_date:
        new_entry = [current_date]
        for project in projects:
            new_entry.append(0)
        histogram.append(new_entry)
        current_date = current_date + datetime.timedelta(days=1)

    # Filling the histogram
    for task in tasks:
        # Finds the line
        for entry in histogram:
            if entry[0] == task.start_date:
                # Finds the column
                for i in range(len(projects)):
                    if projects[i] == task.project_name:
                        # Conversion to minutes
                        entry[1] += (task.duration.seconds + 24*3600*task.duration.days) / 60
                        entry[i + 1] += (task.duration.seconds + 24*3600*task.duration.days) / 60
                        continue
                continue

    # Accumulating the values if needed
    if accumulate:
        for i in range(len(histogram) - 1):
            for j in range(len(histogram[i + 1]) - 1):
                histogram[i + 1][j + 1] += histogram[i][j + 1]

    context = {
        "projects": projects,
        "dated_tasks": histogram
    }
    return render(request, 'StatViz/line_per_project.html', context)


def line_per_project(request):
    return sub_line_per_project(request)


def line_per_project_accumulate(request):
    return sub_line_per_project(request, accumulate=True)
