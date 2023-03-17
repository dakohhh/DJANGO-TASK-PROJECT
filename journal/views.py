from django.http import HttpResponse, HttpRequest

from django.shortcuts import render, redirect

from . forms import CreateUserForm







def home(request:HttpRequest): 
    return render(request, "index.html")


def register(request:HttpRequest): 

    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponse("User registration was successful")
    context = {"form":form}
    
    return render(request, "register.html", context)




