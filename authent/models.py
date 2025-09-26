from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=17, unique=True)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.username