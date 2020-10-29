from django.shortcuts import render
from django.http import HttpResponse

def QuizMake(request):
    return render(request,'QuizMake.html')
