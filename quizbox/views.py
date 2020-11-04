from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import QuestionForm,TestForm
from django.forms import formset_factory
from .models import Test,Question
from django.contrib import messages

def QuizMake(request):
    test_form=TestForm()
    # addques=QuestionForm()
    if request.method=='POST':
        filled_form=TestForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            filled_form_id=filled_form.save()
            filled_form_pk=filled_form_id.id
            messages.success(request, 'Your test details saved.You can add questions for test click on add question button....')
            note='Test Details Add Successfuly !'
            return render(request,'QuizMake.html',{'filled_form_pk':filled_form_pk,'note':note})
        else:
            note='Something went wrong !'
            messages.warning(request,'Please go back and fill all field correctly')
            return render(request,'QuizMake.html',{'note':note})
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
            messages.success(request,'Your Questions is Saved Successfully')
            return HttpResponseRedirect('/edit')
        else:
            messages.warning(request,'Fill all field required go back and fill now ')
        # return render(request,'QuizMake.html',{'note':note})
            return HttpResponseRedirect('/edit')
    return render(request,'QuizMake.html',{'forms':formset})
def edit(request):
    return render(request,'edit.html')
def manage(request):
    test=Test.objects.all()
    return render(request,'manage.html',{'test':test})
def delete_test(request,pk):
    test=Test.objects.get(id=pk).delete()
    messages.success(request,'delete succesfully ')
    return HttpResponseRedirect('/edit')
def edit_test(request,pk):
    test=Test.objects.get(id=pk)
    return render(request,'edit.html',{'test':test})