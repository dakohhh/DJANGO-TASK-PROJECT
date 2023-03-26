from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

from django import forms

from django.contrib.auth.forms import AuthenticationForm

from django.forms.widgets import PasswordInput, TextInput

from . models import Thought, Profile




# - Create User Form

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]



# - Login User Form (login a user)

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())



# - Post a thought 


class ThoughtPostForm(forms.ModelForm):
    class Meta:
        model = Thought
        fields = ["title", "content"]
        exclude = ["user"]


# - Update a thought 

class ThoughtUpdateForm(forms.ModelForm):
     class Meta:
        model = Thought
        fields = ["title", "content"]
        exclude = ["user"]


# - Update User Form  

class UpdateUserForm(forms.ModelForm):

    password = None
    class Meta:
        model = User
        fields = ["username", "email",]
        exclude = ["password1", "password2",]



# Update your profile picture
class UpdateProfileForm(forms.ModelForm):

    profile_pic = forms.ImageField(widget=forms.FileInput(attrs={"class": "form-control-file"}))


    class Meta:
        model = Profile
        fields = ["profile_pic"]




