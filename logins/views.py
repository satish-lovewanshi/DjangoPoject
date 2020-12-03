from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from .models import Student,Teacher,User,Code,Branch,Year,User
from . forms import StudentLoginForm,TeacherLoginForm,StudentSingUpForm,TeacherSignUpForm,StudentProfile,TeacherProfile 

def LoginPage(request):
    LoginForm=AuthenticationForm()
    return render(request,'login.html',{'LoginForm':LoginForm})
def StudentLogin(request):
    
    if request.method == 'POST':
        username1=request.POST['username']
        password1=request.POST['password']
        user=auth.authenticate(username=username1,password=password1)
        if user is not None :
            login(request,user)
            request.session['user']=user.username
            # messages.success(request,"you are logged in success! with username:")
            return redirect('/')
        else:
            messages.info(request,"Username and Password is Wrong please Try again !")
            return redirect('LoginPage')
def LogoutUser(request):
    del request.session['user']
    if 'test_id' in request.session:
        del request.session['test_id']
    logout(request)
    return redirect('LoginPage')       

def signup_as(request):
    return render(request,'signup_as.html')

def StudentSignUp(request):
    student=StudentSingUpForm()
    if request.method == "POST":
        filled_form=StudentSingUpForm(request.POST)
        if filled_form.is_valid():
            user=filled_form.save(commit=False)
            user.is_student=True
            user.save()
            student=Student.objects.create( user=user,college_code=Code.objects.get(id=1),branch=Branch.objects.get(id=1),year=Year.objects.get(id=1))
            student.save()
            # messages.success(request,"Dear Student you are successfully register ")
            username1=request.POST['username']
            password1=request.POST['password2']
            user=auth.authenticate(username=username1,password=password1)
            if user is not None :
                login(request,user)
                request.session['user']=user.username
                # messages.success(request,"you are logged in success! with username:")
                return redirect('/')   
        else:
            if len( request.POST['username']) > 15:
                messages.warning(request,'Username must be less than 15 charecters ') 
            if request.POST['username'] == request.POST['password1'] == request.POST['password2'] :
                messages.warning(request,'Username and Password must be different')
            if request.POST['password1'] != request.POST['password2'] :
                messages.warning(request,'Password confirmation are not same !')
            
            return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
            # return render(request,'StudentSignUp.html',{'StudentSingUpForm':student})
    else:
        return render(request,'StudentSignUp.html',{'StudentSingUpForm':student})
    
def UpdateProfile(request):
    if request.method == "POST":
        if request.user.is_student == True :        
            ProfileForm=Student.objects.get(user=request.user)
            filled_form=StudentProfile(request.POST,instance=ProfileForm)
        if request.user.is_teacher == True :
            ProfileForm=Teacher.objects.get(user=request.user)
            filled_form=TeacherProfile(request.POST,instance=ProfileForm)
        
        if filled_form.is_valid(): 
            fm=filled_form.save(commit=False)
            fm.profile_update = True
            fm.save()
            user=User.objects.get(username=request.user)
            user.profile_update=True
            user.save()
            return redirect('/')
    else:
        if request.user.is_student == True :        
            user=Student.objects.get(user=request.user)
            ProfileForm=StudentProfile(instance=user)
        if request.user.is_teacher == True :
            user=Teacher.objects.get(user=request.user)
            ProfileForm=TeacherProfile(instance=user)
        return render(request,'UpdateProfile.html',{'ProfileForm':ProfileForm})


def TeacherSignUp(request):
    teacher=TeacherSignUpForm()
    if request.method == "POST":
        filled_form=TeacherSignUpForm(request.POST)
        if filled_form.is_valid():
            user=filled_form.save(commit=False)
            user.is_teacher=True
            user.save()
            teacher=Teacher.objects.create(user=user,college_code=Code.objects.get(id=1),branch=Branch.objects.get(id=1))
            teacher.save()
            messages.success(request,"your are successfully register ")
            username1=request.POST['username']
            password1=request.POST['password2']
            user=auth.authenticate(username=username1,password=password1)
            if user is not None :
                login(request,user)
                request.session['user']=user.username
                messages.success(request,"you are logged in success! with username:")
                return redirect('/')
        else:
            if len( request.POST['username']) > 15:
                messages.warning(request,'Username must be less than 15 charecters ') 
            if request.POST['username'] == request.POST['password1'] == request.POST['password2'] :
                messages.warning(request,'Username and Password must be different')
            if request.POST['password1'] != request.POST['password2'] :
                messages.warning(request,'Password confirmation are not same !')
            
            return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
    else:
        return render(request,'TeacherSignUp.html',{'TeacherSignUpForm':teacher})
    
def ranking(request):
    # work in progress 
    return render(request,'ranking.html')