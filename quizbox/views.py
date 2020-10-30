from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import QuestionForm,TestForm

def QuizMake(request):
    form=TestForm()
    return render(request,'QuizMake.html',{'forms':form})
def AddQues(request):
    form=QuestionForm()
    return render(request,'AddQues.html',{'forms':form})  #redierct making 
