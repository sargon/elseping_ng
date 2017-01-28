from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.functions import Now
from django.utils.timezone import now

from . import models

# Create your views here.
def index(request):
    return render(request,"tasks/index.html")

def select(request):
    next_task = models.Task.objects.filter(next_repeat__lte=Now()).order_by('next_repeat').first()
    if next_task is not None:
        next_task.last_complete = now()
        next_task.save()
        return render(request,"tasks/select.html",context={
            'next_task': next_task
        })
    else:
        return render(request, "tasks/select.html", context={
            'next_task': None
        })

