from django import views
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('ad',views.ad,name='ad'),
    path('adsubject',views.adsubject,name='adsubject'),
    path('addquestion',views.addquestion,name='addquestion'),
    path('pythonexam',views.pythonexam,name='pythonexam'),
    path('cppexam',views.cppexam,name='cppexam'),
    path('datastructuresexam',views.datastructuresexam,name='datastructuresexam'),
    path('cexam',views.cexam,name='cexam'),
]