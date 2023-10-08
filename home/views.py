from django.shortcuts import render,HttpResponse
from home.models import Task

def home(request):
    context = {'success' : False, 'name' : "Niladree"}
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        ins = Task(taskTitle = title , tastDesc = desc)
        ins.save()
        context = {'success' : True}
    return render(request, 'index.html', context)

def tasks(request):
    alltasks = Task.objects.all() # ORM Query
    context = {'tasks' : alltasks}
    return render(request, 'tasks.html' , context)

