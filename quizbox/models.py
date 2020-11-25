from django.db import models
from logins.models import Branch,User


class Answer(models.Model):
    ans=models.CharField(max_length=10)

    def __str__(self):
        return self.ans
    
class Test(models.Model):
    teacher_id=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    test_code=models.CharField(max_length=30)
    branch=models.ForeignKey(Branch,on_delete=models.CASCADE)
    number_of_questions=models.IntegerField()
    marks=models.IntegerField()

class Question(models.Model):
    question=models.CharField(max_length=2000)
    option_A=models.CharField(max_length=1000)
    option_B=models.CharField(max_length=1000)
    option_C=models.CharField(max_length=1000)
    option_D=models.CharField(max_length=1000)
    answer=models.ForeignKey(Answer,on_delete=models.CASCADE)
    test=models.IntegerField()
 
