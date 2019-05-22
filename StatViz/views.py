from django.shortcuts import render
from django.shortcuts import HttpResponse
from db import init as init_db
import StatViz.views_utils as vu
import datetime

from StatViz.models import Task

# TODO Make the user enable/disable the "ALL" project
# TODO Make the user change the start and the end of the chart

def init(request):
    context = {}
    init_db.reset()
    return HttpResponse("Init completed!")


def index(request):
    context = {}
    return render(request, 'StatViz/dashboard.html', context)


def sub_line_per_project(request, accumulate=False):
    print(request.GET)

    tasks = Task.objects.all()

    # Building the list of the projects names and getting the first and last dates
    projects, first_date, last_date = vu.projects_list(tasks)

    # Building as an histogram all the dates
    histogram = vu.generate_empty_histogram(first_date, last_date, len(projects))

    # Filling the histogram
    histogram = vu.fill_histogram(histogram, tasks, projects)

    # Accumulating the values if needed
    if accumulate:
        histogram = vu.accumulate_histogram(histogram)

    context = {
        "projects": projects,
        "dated_tasks": histogram
    }
    return render(request, 'StatViz/line_per_project.html', context)


def line_per_project(request):
    return sub_line_per_project(request)


def line_per_project_accumulate(request):
    return sub_line_per_project(request, accumulate=True)
