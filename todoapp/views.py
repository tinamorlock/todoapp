from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from . models import Task

def index(request):
    task_list = Task.objects.order_by('-created')
    context = {
        'task_list': task_list,
    }
    return render(request, 'index.html', context)

def detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'detail.html', {'task': task})


def complete(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        complete_value = request.POST.get('complete')
        if complete_value == 'true':
            task.complete = True
        elif complete_value == 'false':
            task.complete = False
        task.save()
    return render(request, 'detail.html', {'task': task})

def add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        task = Task(title=title, description=description)
        task.save()
        return render(request, 'detail.html', {'task': task})
    return render(request, 'add.html')


def update(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        complete = request.POST.get('complete')
        task.title = title
        task.description = description
        if complete == 'true':
            task.complete = True
        elif complete == 'false':
            task.complete = False
        task.save()
        return render(request, 'detail.html', {'task': task})
    return render(request, 'update.html', {'task': task})


def delete(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        task.delete()
        task_list = Task.objects.order_by('-created')[:5]
        context = {
            'task_list': task_list,
        }
        return render(request, 'index.html', context)
    return render(request, 'delete.html', {'task': task})


def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = User(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
        user.save()
        return render(request, 'index.html')
    return render(request, 'signup.html')


def auth_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print('Received username:', username)
        print('Received password:', password)

        user = authenticate(username=username, password=password)
        print (user)
        if user:
            print('user is not none')
            login(request, user)
            return redirect('todoapp:welcome')
        else:
            messages.error(request, 'Invalid username or password.')
    print('auth_login called')
    return render(request, 'login.html')


def welcome(request):
    return render(request, 'welcome.html')