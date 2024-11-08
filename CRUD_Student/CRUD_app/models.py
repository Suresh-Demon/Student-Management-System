from django.db import models

# Create your models here.

class student(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    mobile=models.CharField(max_length=20)
    address=models.CharField(max_length=200)
    course=models.CharField(max_length=100)
