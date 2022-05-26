from django import forms
from SEapp.models import *

class add_subject(forms.ModelForm):
    class Meta:
        model = Examsubjects
        fields = ["Subject1","Subject2","Subject3","Subject4"]
class add_questions(forms.ModelForm):
    class Meta:
        model = PythonQuestions
        fields = ["question1","question2","question3","question4"]