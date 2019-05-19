from django import db
from StatViz.models import Task
from db import prettify_data
import time


def reset():
    Task.objects.all().delete()
    print("Deletion complete!")

    f = open("db/data", "r", encoding='utf8')
    raw_data = f.read()
    f.close()

    start_time = 0
    i = 0
    for line in prettify_data.raw_to_pretty_data(raw_data):
        i += 1
        task = Task(
            id=line[0],
            name=line[6],
            project_name=line[5],
            start_date=line[1],
            start_time=line[2],
            duration=line[3],
            pause_duration=line[7]
        )
        if time.time() - start_time > 1:
            start_time = time.time()
            db.connections.close_all()
            print(str(i) + " " + task.name)
        task.save()