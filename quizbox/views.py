from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import QuestionForm,TestForm,NumberOfQues
from django.forms import formset_factory

def QuizMake(request):
    form=TestForm()
    addques=QuestionForm()
    if request.method=='POST':
        filled_form=TestForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            filled_form_id=filled_form.save()
            filled_form_pk=filled_form_id.id
            count=filled_form_id.number_of_questions
            PizzaFormSet = formset_factory(QuestionForm,extra=count)
            formset=PizzaFormSet()
            return render(request,'QuizMake.html',{'forms':formset,'filled_form_id':filled_form_pk}) 
    else:
        return render(request,'QuizMake.html',{'forms':form,'form':addques})
def AddQues(request):
    # form=QuestionForm()
    number_of_ques=0 #set default 0pizzas
    noq= NumberOfQues(request.GET)
    if noq.is_valid():
        number_of_ques = noq.cleaned_data['number']
    QuesFormSet = formset_factory(QuestionForm,extra=number_of_ques)
    formset=QuesFormSet()

    return render(request,'QuizMake.html',{'forms':formset})  #redierct making 
