from django.shortcuts import render,redirect
from datetime import datetime, timedelta
from main.models import Task
from main.forms import TaskForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def toDoReturn(request):
    tasks = Task.objects.order_by('-name')
    context = {
        'list': tasks
    }
    return render(request, 'todo_list.html', context)

@login_required
def toDelete(request, id):
    Task.objects.get(pk=id).delete()
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return redirect('task_list')

@login_required
def newTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
        context = {
            'form': form
        }
    return render(request, 'createTask.html', context)

@login_required
def toChange(request, id):
    task = Task.objects.get(pk = id);
    if task.mark == True:
        task.mark = False
    else:
        task.mark = True
    task.save()
    return redirect('task_list')

@login_required
def toReturnCompleted(request):
    tasks = Task.objects.all()
    context = {
        'list':tasks
    }
    return render(request, 'todo_list_completed.html', context)



