from django.shortcuts import render, redirect
from .models import task
from django.contrib import messages
# Create your views here.

def home(request):
    tasks = task.objects.all()
    return render(request, 'main.html', {'tasks': tasks})

def addTask(request):
    task_name = request.POST['txtname']
    task_description = request.POST['txtdescription']
    ntask = task.objects.create(task_name=task_name, task_description=task_description)
    messages.success(request, 'Task added successfully')
    return redirect('/')

def deleteTask(request, task_name):
    task.objects.get(task_name=task_name).delete()
    messages.success(request, 'Task deleted successfully')
    return redirect('/')

def editTask(request, task_name):
    ntask = task.objects.get(task_name=task_name)
    return render(request, 'editTask.html', {'ntask': ntask})

def editingTask(request):
    task_name = request.POST['txtname']
    task_description = request.POST['txtdescription']

    ntask = task.objects.get(task_name=task_name)
    ntask.task_name = task_name
    ntask.task_description = task_description
    ntask.save()
    messages.success(request, 'Task edited successfully')
    return redirect('/')

def done(request, task_name):
    ntask = task.objects.get(task_name=task_name)
    ntask.task_completed = not ntask.task_completed 
    ntask.save()
    return redirect('/')

    