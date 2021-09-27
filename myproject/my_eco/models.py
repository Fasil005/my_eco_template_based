from django.db import models as md
from accounts.models import User
import datetime
import pytz
tz = pytz.timezone('Asia/Calcutta')
# Create your models here.


class Statements(md.Model):

    id = md.AutoField(primary_key=True)
    date = md.CharField(max_length=100,default=datetime.datetime.now(tz=tz).strftime('%Y-%m-%d %I:%M %p'))
    amount = md.FloatField()
    type = md.CharField(max_length=100)
    purpose = md.CharField(max_length=100)
    balance = md.FloatField()
    u_id = md.ForeignKey(User,on_delete=md.CASCADE,null=True)