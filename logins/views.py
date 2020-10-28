from django.shortcuts import render
from django.http import HttpResponse
from . forms import StudentRegForm,TeacherRegForm

def login(request):
    return render(request,'login.html')
def register(request):
    StudentSignup=StudentRegForm()
    return render(request,'register.html',{'StudentRegFrom':StudentSignup})
