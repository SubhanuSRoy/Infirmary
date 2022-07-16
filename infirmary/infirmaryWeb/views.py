# all the import statements to make the functions work in python
from multiprocessing import context
from unicodedata import name
from django.shortcuts import render, redirect
from .models import Record
from django.core import serializers

# function to show/render the form where you add the new record
def add(request):
    return render(request,'add.html')

# function to show the home page of the website
def index (request):
    return render(request,'index.html')

# function to add a new student
def addStudent (request):
    studentfName = request.POST['fname']
    studentlName = request.POST['lname']
    grade = request.POST['grade']
    section = request.POST['section']
    hname = request.POST['hname']
    treatment = request.POST['treatment']
    purpose = request.POST['purpose']

    # code to add a new record to the database
    new_record = Record.objects.create(fname=studentfName,lname=studentlName,grade=grade,section=section,hname=hname,treatment=treatment)
    new_record.save()

    # if saving is successfull then return to the home page
    return redirect('/')

# function to search for student
def searchDB (request):
    studentfname = request.POST['fname']
    studentlname = request.POST['lname']
    data = serializers.serialize("python",Record.objects.filter(fname=studentfname,lname=studentlname))
    context={
        "data":data
    }
    return render(request,'view.html',context)



    