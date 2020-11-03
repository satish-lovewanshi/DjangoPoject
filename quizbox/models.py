from django.db import models

class Test(models.Model):
    subject=models.CharField(max_length=100)
    code=models.CharField(max_length=30)
    number_of_questions=models.IntegerField()
class Question(models.Model):
    question=models.CharField(max_length=2000)
    option_A=models.CharField(max_length=1000)
    option_B=models.CharField(max_length=1000)
    option_C=models.CharField(max_length=1000)
    option_D=models.CharField(max_length=1000)
    answer=models.CharField(max_length=1000)
    # test_id=models.ForeignKey(Test,on_delete=models.CASCADE,to_field='id')
 
