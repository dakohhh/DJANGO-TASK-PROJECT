from django.http import HttpResponse

from django.http.request import HttpRequest

from django.shortcuts import render, redirect

from .models import Task

from .forms import TaskForm , CreateUserForm


from django.contrib.auth.models import User
# Create your views here.



def home(request): 
    return render(request, "index.html")




def task(request:HttpRequest):

    get_all_task = Task.objects.all()

    return render(request, "task.html", {"tasks": get_all_task})


def create_task(request:HttpRequest):
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("task")

    context = {"form": form}


    return render(request, "create_task.html", context)


def update_task(request:HttpRequest, id:int):

    task = Task.objects.get(id=id)

    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect("task")
    

    context = {"form": form}
    return render(request, "update_task.html", context)



def delete_task(request:HttpRequest, id:int):
    
    task = Task.objects.get(id=id)

    if request.method == "POST":
        task.delete()

        return redirect("task")
    
    return render(request, "delete_task.html")





def register(request:HttpRequest):
    
    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect()

    context = {"form":form}

    return render(request, "register.html", context)
     