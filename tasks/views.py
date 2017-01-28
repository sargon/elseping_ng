from django.shortcuts import render
from django.http import HttpResponse

from . import models

# Create your views here.
def index(request):
    return render(request,"tasks/index.html")

def select(request):
    tasks = models.Task.objects.all()
    return render(request,"tasks/view.html")
