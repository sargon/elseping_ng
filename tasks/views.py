from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models.functions import Now
from django.utils.timezone import now

from . import models

# Create your views here.
def index(request):
    return render(request,"tasks/index.html")

def task_view(request,task_id):
    task = models.Task.objects.get(id=task_id)
    return render(request,"tasks/view.html",context={
            'task': task,
           'ball_number': 42,
    })

def task_next(request,ball_number = None):
    task = get_next_task()
    if task is not None:
        task_id = task.id
        return HttpResponseRedirect(reverse(task_view, args=(task_id,)))
    else:
        return render(request, "tasks/notask.html")

def task_complete(request,task_id):
    task = models.Task.objects.get(id=task_id)
    task.last_complete = now()
    task.save()
    if not task.is_needed():
        task.decrease_factor()
        task.save()
    task_id = task.id
    return HttpResponseRedirect(reverse(task_view, args=(task_id,)))

def task_noneed(request,task_id):
    task = models.Task.objects.get(id=task_id)
    if task.is_needed():
        task.increase_factor()
        task.save()
    task_id = task.id
    return HttpResponseRedirect(reverse(task_view, args=(task_id,)))


# Utilities

def get_next_task():
    return models.Task.objects.filter(next_repeat__lte=Now()).order_by('next_repeat').first()