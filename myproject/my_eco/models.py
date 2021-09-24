from django.db import models as md

# Create your models here.

class Statements(md.Model):

    id = md.AutoField(primary_key=True)
    date = md.DateTimeField(auto_now_add=True)
    amount = md.FloatField()
    type = md.CharField(max_length=100)
    purpose = md.CharField(max_length=100)
    balance = md.FloatField()