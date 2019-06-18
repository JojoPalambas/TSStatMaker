import datetime


def filter_tasks(tasks):
    ret = []
    for task in tasks:
        ret.append(task)
    return ret


def projects_list(tasks):
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
    return projects, first_date, last_date


def tasks_list(tasks):
    tasks_names = ["ALL"]
    first_date = datetime.datetime.now().date()
    last_date = datetime.date(1970, 1, 1)
    for task in tasks:
        task.project_name = task.project_name + " - " + task.name
        # Project-listing part
        placed = False
        for task_name in tasks_names:
            if task_name == task.project_name:
                placed = True
                continue
        if not placed:
            tasks_names.append(task.project_name)

        # Date extremums part
        if task.start_date < first_date:
            first_date = task.start_date
        if task.start_date > last_date:
            last_date = task.start_date
    return tasks_names, first_date, last_date


def generate_empty_histogram(first_date, last_date, projects_nb):
    histogram = []
    current_date = first_date
    while current_date <= last_date:
        new_entry = [current_date]
        for i in range(projects_nb):
            new_entry.append(0)
        histogram.append(new_entry)
        current_date = current_date + datetime.timedelta(days=1)
    return histogram


def fill_histogram(histogram, tasks, projects):
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
    return histogram


def accumulate_histogram(histogram):
    for i in range(len(histogram) - 1):
        for j in range(len(histogram[i + 1]) - 1):
            histogram[i + 1][j + 1] += histogram[i][j + 1]
    return histogram
