from operator import mod
from pyexpat import model
from django.db import models


class Examsubjects(models.Model):
    Subject1 = models.CharField(max_length=20)
    Subject2 = models.CharField(max_length=20)
    Subject3 = models.CharField(max_length=20)
    Subject4 = models.CharField(max_length=20)

class PythonQuestions(models.Model):
    question1 = models.CharField(max_length=100)
    question2=models.CharField(max_length=100)
    question3=models.CharField(max_length=100)
    question4=models.CharField(max_length=100)
         
class results(models.Model):
    idnum =models.IntegerField()
    score = models.IntegerField()