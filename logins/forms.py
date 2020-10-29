from django import forms
from .models import StudentReg,TeacherReg,Branch

class StudentRegForm(forms.ModelForm):
    class Meta:
        model=StudentReg
        fields=['college_code','name','roll_number','branch','year','mobile']
        # labels={}
        widgets={
            'college_code': forms.Select(attrs={'class':'form-control','placeholder':'Enter college code'}),
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'roll_number': forms.TextInput(attrs={'class':'form-control'}),
            'branch': forms.Select(attrs={'class':'form-control'}),
            'year': forms.Select(attrs={'class':'form-control'}),
            'mobile': forms.TextInput(attrs={'class':'form-control'}),        
        }
class TeacherRegForm(forms.ModelForm):
    
    class Meta:
        model = TeacherReg
        fields='__all__'
        widgets={
            'college_code': forms.Select(attrs={'class':'form-control','placeholder':'Enter college code'}),
            'branch': forms.Select(attrs={'class':'form-control'}),
            'pass_number': forms.TextInput(attrs={'class':'form-control'}),
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'mobile': forms.TextInput(attrs={'class':'form-control'}),
        }
class StudentLoginForm(forms.ModelForm):
    class Meta:
        model=StudentReg
        fields=['college_code','roll_number','mobile']
        # labels={}
        widgets={
            'college_code': forms.Select(attrs={'class':'form-control','placeholder':'Enter college code'}),
            'roll_number': forms.TextInput(attrs={'class':'form-control'}),
            'mobile': forms.TextInput(attrs={'class':'form-control'}),        
        }
class TeacherLoginForm(forms.ModelForm):
    class Meta:
        model = TeacherReg
        exclude=('branch','name')
        widgets={
            'college_code': forms.Select(attrs={'class':'form-control','placeholder':'Enter college code'}),
            'pass_number': forms.TextInput(attrs={'class':'form-control'}),
            'mobile': forms.TextInput(attrs={'class':'form-control'}),
        }

    
