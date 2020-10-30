from django import forms
from .models import Test,Question

class QuestionForm(forms.ModelForm):
    
    class Meta:
        model = Question
        exclude =('test_id',)
class TestForm(forms.ModelForm):
    
    class Meta:
        model = Test
        fields = ('__all__')

