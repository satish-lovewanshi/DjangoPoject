from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import QuestionForm,TestForm
from django.forms import formset_factory
from .models import Test,Question
from logins.models import User,Student,Teacher
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='LoginPage')
def QuizMake(request):
    test_form=TestForm()
    # addques=QuestionForm()
    if request.method=='POST':
        filled_form=TestForm(request.POST)
        if filled_form.is_valid():
            fm=filled_form.save(commit=False)
            fm.teacher_id=request.session['user']
            fm.save()
            filled_form_id=filled_form.save()
            filled_form_pk=filled_form_id.id
            
            messages.success(request, 'Your test details saved.You can add questions for test click on add question button....')
            note='Test Details Add Successfuly !'
        return render(request,'QuizMake.html',{'filled_form_pk':filled_form_pk,'note':note,'forms':test_form})
    else:
        return render(request,'QuizMake.html',{'forms':test_form})

@login_required(login_url='LoginPage')
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
            return HttpResponseRedirect('/manage_test')
        else:
            messages.warning(request,'Fill all field required go back and fill now ')
        # return render(request,'QuizMake.html',{'note':note})
            return HttpResponseRedirect('/edit')
    return render(request,'QuizMake.html',{'forms':formset})
@login_required(login_url='LoginPage')
def edit(request):
    return render(request,'edit.html')
    
@login_required(login_url='LoginPage')
def manage_test(request):
    branch=Teacher.objects.get(user=User.objects.get(username=request.user).id).branch
    test=Test.objects.filter(branch=branch)
    return render(request,'manage_test.html',{'test':test})

@login_required(login_url='LoginPage')
def manage_student(request):
    branch=Teacher.objects.get(user=User.objects.get(username=request.user).id).branch
    students=Student.objects.filter(branch=branch)
    return render(request,'manage_student.html',{'students':students})

@login_required(login_url='LoginPage')
def remove_student(request,pk):
    students=Student.objects.get(user=pk).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

@login_required(login_url='LoginPage')
def delete_test(request,pk):
    test=Test.objects.get(id=pk).delete()
    messages.success(request,'Test delete succesfully !')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
    
@login_required(login_url='LoginPage')
def delete_ques(request,pk):
    Question.objects.get(id=pk).delete()
    messages.success(request,"Question delete successfully !")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

@login_required(login_url='LoginPage')
def edit_test(request,pk):
    if request.method == 'POST':
        test=Test.objects.get(pk=pk)
        test_form=TestForm(request.POST,instance=test)
        if test_form.is_valid():
            test_form.save()
            messages.success(request,"Test deatils is successfully Updated !")
        return HttpResponseRedirect('/manage_test')
    else:
        test=Test.objects.get(pk=pk)
        test_form=TestForm(instance=test)
    return render(request,'QuizMake.html',{'test_form':test_form})
@login_required(login_url='LoginPage')
def manage_ques(request,pk):
    ques=Question.objects.filter(test=pk)
    return render (request,'manage_ques.html',{'ques':ques})
@login_required(login_url='LoginPage')
def edit_ques(request,pk):
    if request.method == 'POST':
        ques=Question.objects.get(id=pk)
        ques_form=QuestionForm(request.POST,instance=ques)
        if ques_form.is_valid():
            ques_form.save()
            messages.success(request,"Question details is successfully Updated ! ")
        return HttpResponseRedirect('/manage_test')        
    else:
        ques=Question.objects.get(id=pk)
        ques_form=QuestionForm(instance=ques)
    return render(request,'QuizMake.html',{'ques_update_form':ques_form})