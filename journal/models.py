from django.db import models

from django.contrib.auth.models import User
# Create your models here.



class Thought(models.Model):
    title = models.CharField(max_length=85)

    content = models.CharField(max_length=255)

    date_posted = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, max_length=10, on_delete=models.CASCADE)


