from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    # Current repeating factor
    repeat_factor = models.PositiveIntegerField()
    # Maximal repeating factor 
    max_repeat_factor = models.PositiveIntegerField()
