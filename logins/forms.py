from django import forms
from .models import StudentReg,TeacherReg

class StudentRegForm(forms.ModelForm):
    class Meta:
        model=StudentReg
        fields=['college_code','name','roll_number','branch','year','mobile']
        # labels={}
class TeacherRegForm(forms.ModelForm):
    
    class Meta:
        model = TeacherReg
        fields = ()
