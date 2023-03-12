from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class student(models.Model):
    booked_by=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=100)
    admno=models.PositiveIntegerField()
    email=models.EmailField()
    paremail=models.EmailField()
    phno=models.PositiveBigIntegerField()
    p_phno=models.PositiveBigIntegerField()
    sex=models.CharField(max_length=25)
    branch=models.CharField(max_length=100)
    year=models.CharField(max_length=5)
    l_type=models.CharField(max_length=100)
    l_datefrom=models.DateField()
    l_dateto=models.DateField()
    l_rsn=models.TextField()
    closed=models.BooleanField(default='False',null=True)
    permit_allowed=models.BooleanField(default='False',null=True)