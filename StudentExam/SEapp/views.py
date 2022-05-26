from urllib import request
from django.shortcuts import render
from SEapp.forms import *

def home(request):
    return render(request,'home.html')

def ad(request):
    subjects = Examsubjects.objects.all()
    return render(request,'adsection/ad_dashboard.html',{'subjects':subjects})  
def addquestion(request):
    form =add_questions()
    if request.method=='POST':
        form = add_questions(request.POST)
        if form.is_valid():
            form.save()
    else:
        form =add_questions()        
        return render(request,'adsection/addquestion.html',{'form':form})
def adsubject(request):
    form = add_subject()
    if request.method == 'POST':
        form = add_subject(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = add_subject()
    return render(request,'adsection/ad_subject.html',{'form':form})         
def viewresults():
    data=results.objects.all()
    return render(request,'viewresults.html',{'data':data})
def pythonexam(request):
    return render(request,'Exam/pythonexam.html')

def cppexam(request):
    return render(request,'Exam/cppexam.html')

def datastructuresexam(request):
    return render(request,'Exam/datastructuresexam.html')

def cexam(request):
    return render(request,'Exam/cexam.html')
# Create your views here.

