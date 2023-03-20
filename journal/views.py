from django.http import HttpRequest

from django.shortcuts import render, redirect

from . forms import CreateUserForm, LoginForm, ThoughtPostForm, ThoughtUpdateForm, UpdateUserForm

from . models import Thought

from django.contrib.auth.models import User


from django.contrib import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

from django.contrib import messages





def home(request:HttpRequest): 
    return render(request, "index.html")


def register(request:HttpRequest): 

    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            
            messages.success(request, "Congrats your account is created..login now")
        
            return redirect("login")
    context = {"form":form}

    return render(request, "register.html", context)



def login(request:HttpRequest):

    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get("username")

            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)

                return redirect("dashboard")
            
    context = {'form':form}

    return render(request, "login.html", context)




@login_required(login_url="login")
def dashboard(request:HttpRequest):

    return render(request, "dashboard.html")




@login_required(login_url="login")
def post_thoght(request:HttpRequest):

    form = ThoughtPostForm()

    print(request.user)

    if request.method == "POST":

        form = ThoughtPostForm(request.POST)

        if form.is_valid():

            thought = form.save(commit=False)

            thought.user = request.user

            thought.save()

        return redirect("dashboard")
    

    context= {'form':form}

    return render(request, "post_thought.html", context)

@login_required(login_url="login")
def update_thoght(request:HttpRequest, id:int):

    thought = Thought.objects.get(id=id)

    form = ThoughtUpdateForm(instance=thought)

    if request.method == "POST":

        form = ThoughtUpdateForm(request.POST, instance=thought)

        if form.is_valid():


            form.save()

            return redirect("my_thought")
        
    context = {"form":form}

    return render(request, "update_thought.html", context)





@login_required(login_url="login")
def my_thought(request:HttpRequest):

    thought = Thought.objects.all().filter(user=request.user.id)

    context = {"thought": thought}

    return render(request, "mythought.html", context)



@login_required(login_url="login")
def delete_thoght(request:HttpRequest, id:int):

    thought = Thought.objects.get(id=id)

    if request.method == "POST":
        thought.delete()

        return redirect("my_thought")

    return render(request, "delete_thought.html")





@login_required(login_url="login")
def profile_management(request:HttpRequest):
    

    form = UpdateUserForm(instance=request.user)

    if request.method == "POST":

        form = UpdateUserForm(request.POST, instance=request.user)

        if form.is_valid():


            form.save()

            return redirect("dashboard")
        
    context = {"form":form}

    return render(request, "profile-management.html", context)




@login_required(login_url="login")
def delete_account(request:HttpRequest):
    
    if request.method == "POST":

        user = User.objects.get(username=request.user)

        user.delete()

        return  redirect("login")

    return render(request, "delete_account.html")






def logout(request:HttpRequest):
    auth.logout(request)

    return redirect("login")
