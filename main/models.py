from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class MyCartUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField()
    email = models.EmailField()
    last_login_time = models.DateTimeField(auto_now=True)
    creation_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user
