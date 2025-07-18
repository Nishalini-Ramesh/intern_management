
from django.http import HttpResponse

def home(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')
   


from django.shortcuts import render, redirect

# Temporary memory-based task list
task_store = []

def task_list(request):
    return render(request, 'task_list.html', {'tasks': task_store})

def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            task_store.append({'title': title, 'completed': False})
        return redirect('task_list')
    return render(request, 'create_task.html')


