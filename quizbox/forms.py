from django import forms
from django.forms import ModelForm,Textarea
from .models import Test,Question

class QuestionForm(forms.ModelForm):
    
    class Meta:
        model = Question
        exclude =('test',)
        # fields = ('__all__')
        widgets={
            'question':Textarea(attrs={'cols':100,'rows':3}),
            'option_A':Textarea(attrs={'cols':100,'rows':2}),
            'option_B':Textarea(attrs={'cols':100,'rows':2}),
            'option_C':Textarea(attrs={'cols':100,'rows':2}),
            'option_D':Textarea(attrs={'cols':100,'rows':2}),
            
        }
class TestForm(forms.ModelForm):
    
    class Meta:
        model = Test
        fields = ('__all__')

