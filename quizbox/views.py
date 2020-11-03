from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
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
            return render(request,'QuizMake.html',{'filled_form_pk':filled_form_pk})
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
            for form in filled_formset: #we can edit out fillled form using commit=False 
                post=form.save(commit=False)
                post.test=pk
                post.save()
            notes='Your Questions is successfuly saved'
        else:
            notes="Fill all field required go back and fill now !"
        return render(request,'QuizMake.html',{'notes':notes})
        # return HttpResponseRedirect('/quizmake',{'notes':notes})
    return render(request,'QuizMake.html',{'forms':formset})
