from django.db import models as md

# Create your models here.

class User(md.Model):
    id = md.AutoField(primary_key=True)
    email = md.EmailField(max_length=255)
    password = md.CharField(max_length=150)
class Statements(md.Model):

    id = md.AutoField(primary_key=True)
    date = md.DateTimeField(auto_now_add=True)
    amount = md.FloatField()
    type = md.CharField(max_length=100)
    purpose = md.CharField(max_length=100)
    balance = md.FloatField()