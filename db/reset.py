from StatViz.models import Project, Task, Pause
from db import prettify_data


def init():
    f = open("db/data", "r", encoding='utf8')
    raw_data = f.read()
    f.close()

    for d in prettify_data.raw_to_pretty_data(raw_data):
        print(d)
