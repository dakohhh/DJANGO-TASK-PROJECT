from django.urls import path
from . import views

from django.contrib.auth import views as auth_views


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

    # - 1 Reset Password (Allows us to enter our email in order to recieve a password reset link)

    path("reset_password", auth_views.PasswordResetView.as_view(template_name="password_reset/password_reset.html"), name="reset_password"),

    # - 2 Show a success message stating that an email was sent to rest our password

    path("reset_password_sent", auth_views.PasswordResetDoneView.as_view(template_name="password_reset/password_reset_sent.html"), name="password_reset_done"),

    # - 3 Send a link to our email so we can reset our password

    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="password_reset/password_reset_form.html"), name="password_reset_confirm"),

    # - 4  Show a message stating that our password was changed

    path("reset_password_complete", auth_views.PasswordResetCompleteView.as_view(template_name="password_reset/password_reset_complete.html"), name="password_reset_complete"),



]   