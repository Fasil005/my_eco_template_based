from django.db import models as md

# Create your models here.
class User(md.Model):
    id = md.AutoField(primary_key=True)
    email = md.EmailField(max_length=255)
    password = md.CharField(max_length=150)