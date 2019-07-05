from django.db import models

class Task(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    name = models.CharField(max_length=128)
    project_name = models.CharField(max_length=128)
    start_date = models.DateField()
    start_time = models.TimeField()
    duration = models.DurationField()
    pause_duration = models.DurationField()
    tags = models.CharField(max_length=1024, default="")

    def __str__(self):
        return self.name
