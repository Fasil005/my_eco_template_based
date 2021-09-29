from django.db import models as md

# Create your models here.
class User(md.Model):
    id = md.AutoField(primary_key=True)
    fullname = md.CharField(max_length=255)
    username = md.CharField(max_length=255,unique=True)
    password = md.CharField(max_length=150)