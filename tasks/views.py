from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models.functions import Now
from django.utils.timezone import now
from datetime import *


from . import models

# Create your views here.
def index(request):
    return render(request,"tasks/index.html")

def task_view(request,task_id):
    task = models.Task.objects.get(id=task_id)
    return render(request,"tasks/view.html",context={
            'task': task,
    })

def task_view_ball(request,task_id,ball_id):
    task = models.Task.objects.get(id=task_id)
    return render(request,"tasks/view.html",context={
            'task': task,
            'ball_number': ball_id,
    })

def task_list(request):
    all_tasks = models.Task.objects.all()
    tasks_today = []
    tasks_tomorrow = []
    tasks_this_week = []
    tasks_this_month = []
    today = datetime.now().timetuple().tm_yday
    # sorting tasks, beginning with most likely
    for task in all_tasks:
        assert task.repeat_factor <= 30
        if task.next_repeat.timetuple().tm_yday <= today:
            tasks_today.append(task)
        elif task.next_repeat.timetuple().tm_yday == today + 1:
            tasks_tomorrow.append(task)
        elif task.next_repeat.timetuple().tm_yday <= today + 7:
            tasks_this_week.append(task)
        else:
            tasks_this_month.append(task)
    # passing to list.html, where magic happens
    return render(request, 'tasks/list.html', context={
        'tasks_today': tasks_today,
        'tasks_tomorrow': tasks_tomorrow,
        'tasks_this_week': tasks_this_week,
        'tasks_this_month': tasks_this_month,
    })

def task_next(request):
    task = get_next_task()
    ball_id = None
    if request.method == 'POST':
        if 'ball_number' in request.POST:
         ball_id = request.POST['ball_number']
    if task is not None:
        task_id = task.id
        if ball_id is not None:
          return HttpResponseRedirect(reverse(task_view_ball, args=(task_id,ball_id,)))
        else:
          return HttpResponseRedirect(reverse(task_view_ball, args=(task_id,ball_id,)))
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
