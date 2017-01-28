from django.db import models

import datetime

class Task(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    # Last time task has been completed
    last_complete = models.DateTimeField()
    # Current repeating factor
    repeat_factor = models.PositiveIntegerField()
    # Maximal repeating factor 
    max_repeat_factor = models.PositiveIntegerField()

    def get_next_repeat(self):
        timedelta = datetime.timedelta(days=self.repeat_factor)
        return self.last_complete + timedelta