from django.urls import path
from . import views



urlpatterns = [

    # - Homepage
    path('', views.home, name="home"),

    # - Register
    path("register", views.register, name="register"),

    # - Login

    path("login", views.login, name="login"),

    # - Dashboard

    path("dashboard", views.dashboard, name="dashboard"),

    # - Logout

    path("logout", views.logout, name="logout"),

    # - Post Thought

    path("post_thoght", views.post_thoght, name="post_thoght"),

    # - Update Thought
    path("update_thoght/<int:id>", views.update_thoght, name="update_thoght"),

    
    path("delete_thoght/<int:id>", views.delete_thoght, name="delete_thoght"),

    # - My Thoughts

    path("my_thought", views.my_thought, name="my_thought"),

    # - Profile Managements

    path("profile_management", views.profile_management, name="profile_management"),

    
    # - Delete Account

    path("delete_account", views.delete_account, name="delete_account"),



] 