from django.shortcuts import render
from quizbox.models import Test,Question
from django.http import HttpResponse,HttpResponseRedirect
# Create your views .
def home(request):
    test=Test.objects.all()
    return render(request,'home.html',{'test':test})

def start(request,pk):        
    questions=Question.objects.filter(test=pk)
    if request.method=="POST":
        return HttpResponseRedirect('done')
    else:
        return render(request,'start.html',{'questions':questions})
def done(request):
    return HttpResponseRedirect('/home')