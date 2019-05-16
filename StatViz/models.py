from django.db import models

class Project(models.Model):
    id = models.CharField(max_length=32)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=2048)

class Task(models.Model):
    id = models.CharField(max_length=32)
    name = models.CharField(max_length=128)
    nb = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    duration = models.DurationField()
    real_duration = models.DurationField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

class Pause(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
