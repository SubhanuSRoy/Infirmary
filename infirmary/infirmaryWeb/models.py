from statistics import mode
from django.db import models
from datetime import datetime

# Creating the model to store the info of each record
class Record(models.Model):
    # Each is a characters field, where we can decide a maximum length
    fname = models.CharField(max_length=1000)
    lname = models.CharField(max_length=1000)
    grade = models.CharField(max_length=5)
    section = models.CharField(max_length=5)
    hname = models.CharField(max_length=1000)
    treatment = models.CharField(max_length=1000000)
    purpose = models.CharField(max_length=1000,default="General")

    # this is the datetime field which is automatically populated when the form is submitted
    time = models.DateTimeField(default=datetime.now,blank=True)