from StatViz.models import Project, Task, Pause


def init():
    f = open("db/data", "r")
    raw_data = f.read()
    f.close()
