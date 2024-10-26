# tasks/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def task_list(request):
    # Filter tasks based on query parameters
    filter_completed = request.GET.get('completed')
    if filter_completed == 'true':
        tasks = Task.objects.filter(completed=True)
    elif filter_completed == 'false':
        tasks = Task.objects.filter(completed=False)
    else:
        tasks = Task.objects.all()
    
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def mark_task_complete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed  # Toggle completion status
    task.save()
    return redirect('task_list')

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.save()
        return redirect('task_list')
    
    return render(request, 'tasks/edit_task.html', {'task': task})
