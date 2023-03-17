from django.urls import path
from . import views



urlpatterns = [

    #Homepage
    path('', views.home, name="home"),

    # - Register
    path("register", views.register, name="register")



] 