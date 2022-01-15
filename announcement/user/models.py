from django.db import models


class User(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=30)
    avatar = models.ImageField(upload_to='user/', null=True, blank=True)
    date_create = models.DateField(auto_now_add=True)
