from distutils.command.upload import upload
from email.mime import image
from turtle import title
from django.db import models

# Create your models here.

class Card(models.Model):
    title=models.CharField(max_length=200, null=True)
    description=models.EmailField(max_length=200, null=True)
    message=models.CharField(max_length=200, null=True)
    price=models.CharField(max_length=200, null=True)
    upload=models.ImageField(upload_to ='uploads/', default='../default/duplex.jpeg')
    date=models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.title
