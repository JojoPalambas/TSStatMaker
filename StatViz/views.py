from django.shortcuts import render
from django.shortcuts import HttpResponse
from db import init as init_db
import StatViz.views_utils as vu

from StatViz.models import Task

# TODO Make the user enable/disable the "ALL" project
# TODO Make the user change the start and the end of the chart


def init(request):
    init_db.reset()
    return HttpResponse("Init completed!")


def index(request):
    context = {}
    return render(request, 'StatViz/dashboard.html', context)


def sub_line_per_project(request, accumulate=False, data_type="projects"):
    tasks = Task.objects.all()

    # Filtering
    tasks = vu.filter_tasks(tasks)

    # Building the list of the data line names and getting the first and last dates
    data, first_date, last_date = [], "", ""
    if data_type == "projects":
        data, first_date, last_date = vu.projects_list(tasks)
    elif data_type == "tasks":
        data, first_date, last_date = vu.tasks_list(tasks)
    else:
        data, first_date, last_date = vu.projects_list(tasks)

    # Building as an histogram all the dates
    histogram = vu.generate_empty_histogram(first_date, last_date, len(data))

    # Filling the histogram
    histogram = vu.fill_histogram(histogram, tasks, data)

    # Accumulating the values if needed
    if accumulate:
        histogram = vu.accumulate_histogram(histogram)

    context = {
        "data": data,
        "data_type": data_type,
        "dated_tasks": histogram
    }
    return render(request, 'StatViz/line_per_project.html', context)


def show(request):
    raw_tasks = Task.objects.all()
    tasks = []

    for rt in raw_tasks:
        tasks.append({
            "id": rt.id,
            "name": rt.name,
            "project_name": rt.project_name,
            "start_date": rt.start_date,
            "start_time": rt.start_time,
            "duration": rt.duration,
            "pause_duration": rt.pause_duration
        })

    context = {
        "tasks": tasks
    }
    return render(request, 'StatViz/show.html', context)


def line_per_project(request):
    return sub_line_per_project(request)


def line_per_project_accumulate(request):
    return sub_line_per_project(request, accumulate=True)


def line_per_task(request):
    return sub_line_per_project(request, data_type="tasks")
