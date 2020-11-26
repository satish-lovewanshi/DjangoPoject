from django.shortcuts import render
from quizbox.models import Test,Question
from logins.models import Student,User
from .models import Result
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages


def home(request):#show all test for student 
    branch=Student.objects.get(user=User.objects.get(username=request.user).id).branch
    test=Test.objects.filter(branch=branch)
    is_done=Result.objects.filter(student_id=request.session['user'])
    l=[]
    for t in test:
        for i in is_done:
            if t.id == i.test_id:
                l.append(t.id)
    # print('this test done by user ',l)
    return render(request,'home.html',{'test':test,'is_done':l})

def start(request,pk):     #start test this function works session started
    request.session['test_id']=pk  
    questions=Question.objects.filter(test=pk)
    return render(request,'start.html',{'questions':questions})
def done(request):
    correct=0
    wrong=0
    test_id=''
    if request.method == 'POST':
        a_list=request.POST
        attempt=len(a_list)-1    
        for i in a_list:
            if (i == 'csrfmiddlewaretoken'):
                pass
            else:
                questions=Question.objects.get(id=int(i))
                ans=a_list[i]
                c_ans=questions.answer
                test_id=questions.test
                if str(ans) == str(c_ans):
                    correct+=1
                else:
                    wrong+=1
        total_ques=Test.objects.get(id=request.session['test_id']).number_of_questions
        # print(attempt,correct,wrong,total_ques)
        result=Result()
        result.test_id=int(request.session['test_id'])
        result.total_questions=Test.objects.get(id=request.session['test_id']).number_of_questions
        result.attempt=len(a_list)-1 
        result.right=correct
        result.wrong=wrong
        result.marks=Test.objects.get(id=request.session['test_id']).marks
        perQuesMarks=(Test.objects.get(id=request.session['test_id']).marks)/Test.objects.get(id=request.session['test_id']).number_of_questions
        result.score=perQuesMarks*correct
        result.branch=Test.objects.get(id=request.session['test_id']).branch  
        result.student_id=request.user
        result.save()
        messages.warning(request,"Total Attemp :" + str(len(a_list)-1 ))
        messages.success(request,"Right Answer :" + str(correct) )
        messages.warning(request,"Wrong Answer:" + str(wrong))
        messages.success(request,"Score:" + str(perQuesMarks*correct))


        return render(request,'done.html')
    else:
        error="something went wrong !"
        return render(request,'done.html',{'answer':error})

def history(request):
    test=Test.objects.all()
    done_test=Result.objects.filter(student_id=request.session['user'])
    # l=[]
    # r=[]
    # for t in test:
    #     for i in is_done:
    #         if t.id == i.test_id:
    #             l.append(t.id)
    #             r.append(t.marks)
    return render(request,'history.html',{'done_test':done_test})