from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import QuestionForm,TestForm
from django.forms import formset_factory
from .models import Test,Question

def QuizMake(request):
    test_form=TestForm()
    # addques=QuestionForm()
    if request.method=='POST':
        filled_form=TestForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            filled_form_id=filled_form.save()
            filled_form_pk=filled_form_id.id
            # count=filled_form_id.number_of_questions
            # PizzaFormSet = formset_factory(QuestionForm,extra=count)
            # formset=PizzaFormSet()
            # if request.method == 'POST':
            #     filled_formset=PizzaFormSet(request.POST)
                # if filled_formset.is_valid():
                #     for form in filled_formset:
                #         form.save()
                #     note="Pizzas has been ordered !"
                # else:
                #     note="order was not created pls try again"
            # return render(request,'AddQues.html',{'formset':formset,'filled_form_id':filled_form_pk})
            note="you can add your questions click here" 
            return render(request,'QuizMake.html',{'note':note,'filled_form_pk':filled_form_pk})
    else:
        return render(request,'QuizMake.html',{'forms':test_form})
def AddQues(request,pk):
    test_info=Test.objects.get(id=pk)
    count=test_info.number_of_questions
    PizzaFormSet = formset_factory(QuestionForm,extra=count)
    formset=PizzaFormSet()
    if request.method == 'POST':
        filled_formset=PizzaFormSet(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                form.save()
            notes='your questis is save '
        else:
            notes="your question not saved"
        return render(request,'QuizMake.html',{'notes':notes})
    return render(request,'QuizMake.html',{'forms':formset})  #redierct making 
