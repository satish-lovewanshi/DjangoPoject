from django.shortcuts import render
from django.http import HttpResponse
from . forms import StudentRegForm,TeacherRegForm,StudentLoginForm,TeacherLoginForm

def login(request):
    StudentLogin=StudentLoginForm()
    TeacherLogin=TeacherLoginForm()
    return render(request,'login.html',{'StudentLoginForm':StudentLogin,'TeacherLoginForm':TeacherLogin})

def register(request):
    StudentSignup=StudentRegForm()
    TeacherSignup=TeacherRegForm()
    return render(request,'register.html',{'StudentRegFrom':StudentSignup,'TeacherRegForm':TeacherSignup})
