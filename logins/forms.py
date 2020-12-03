from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Branch,Student,Teacher,User
from django.core import validators

class StudentLoginForm(forms.ModelForm):
    class Meta:
        pass
        # model=Student
        # fields=['college_code','roll_number','mobile']
        # # labels={}
        # widgets={
        #     'college_code': forms.Select(attrs={'class':'form-control','placeholder':'Enter college code'}),
        #     'roll_number': forms.TextInput(attrs={'class':'form-control'}),
        #     'mobile': forms.TextInput(attrs={'class':'form-control'}),        
        # }
class TeacherLoginForm(forms.ModelForm):
    class Meta:
        pass
        # model = Teacher
        # exclude=('branch','name')
        # widgets={
        #     'college_code': forms.Select(attrs={'class':'form-control','placeholder':'Enter college code'}),
        #     'pass_number': forms.TextInput(attrs={'class':'form-control'}),
        #     'mobile': forms.TextInput(attrs={'class':'form-control'}),
        # }

class StudentSingUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model=User


class StudentProfile(forms.ModelForm):
    
    class Meta:
        model=Student
        exclude=('profile_update','user')
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Fist Name'}),        
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Last Name'}),        
            'phone':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Phone Number'}),        
            'college_code': forms.Select(attrs={'class':'form-control','placeholder':'Enter college code'}),
            'roll_number': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Roll Number'}),
            'branch': forms.Select(attrs={'class':'form-control'}),
            'year': forms.Select(attrs={'class':'form-control'}),
            'mobile': forms.TextInput(attrs={'class':'form-control'}),        
        }

class TeacherProfile(forms.ModelForm):
    class Meta:
        model=Teacher
        # fields='__all__'
        exclude=('user',)
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Fist Name'}),        
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Last Name'}),        
            'phone':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Phone Number'}),        
            'college_code': forms.Select(attrs={'class':'form-control','placeholder':'Enter college code'}),
            'branch': forms.Select(attrs={'class':'form-control'}),
        }

class TeacherSignUpForm(UserCreationForm):    

    class Meta(UserCreationForm.Meta):
        model=User
        

    

# class StudentRegForm(forms.ModelForm):
#     class Meta:
#         model=StudentReg
#         fields=['college_code','name','roll_number','branch','year','mobile']
#         # labels={}
#         widgets={
#             'college_code': forms.Select(attrs={'class':'form-control','placeholder':'Enter college code'}),
#             'name': forms.TextInput(attrs={'class':'form-control'}),
#             'roll_number': forms.TextInput(attrs={'class':'form-control'}),
#             'branch': forms.Select(attrs={'class':'form-control'}),
#             'year': forms.Select(attrs={'class':'form-control'}),
#             'mobile': forms.TextInput(attrs={'class':'form-control'}),        
#         }
# class TeacherRegForm(forms.ModelForm):
    
#     class Meta:
#         model = TeacherReg
#         fields='__all__'
#         widgets={
#             'college_code': forms.Select(attrs={'class':'form-control','placeholder':'Enter college code'}),
#             'branch': forms.Select(attrs={'class':'form-control'}),
#             'pass_number': forms.TextInput(attrs={'class':'form-control'}),
#             'name': forms.TextInput(attrs={'class':'form-control'}),
#             'mobile': forms.TextInput(attrs={'class':'form-control'}),
#         }
