from django.db import models
from django.utils.timezone import now

import datetime

class Task(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    # Last time task has been completed
    last_complete = models.DateTimeField(default=now)
    # Next repeat
    next_repeat = models.DateTimeField(default=now)
    # Current repeating factor
    repeat_factor = models.PositiveIntegerField(default=7)
    # Maximal repeating factor 
    max_repeat_factor = models.PositiveIntegerField(default=30)

    def get_next_repeat(self):
        timedelta = datetime.timedelta(days=self.repeat_factor)
        return self.last_complete + timedelta

    def is_needed(self):
        return now() > self.get_next_repeat()

    def increase_factor(self):
        self.repeat_factor += 1
        if self.repeat_factor > self.max_repeat_factor:
            self.repeat_factor = self.max_repeat_factor

    def decrease_factor(self):
        self.repeat_factor -= 1
        if self.repeat_factor < 1:
            self.repeat_factor = 1


    def save(self, *args, **kwargs):
        self.next_repeat = self.get_next_repeat()
        super(Task,self).save(*args, **kwargs)

