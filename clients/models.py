from django.db import models

class Client(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=50,unique=True)
    password=models.CharField(max_length=50)
    is_activated= models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)