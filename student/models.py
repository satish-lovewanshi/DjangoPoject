from django.db import models
class Result(models.Model):
    total_questions=models.IntegerField()
    attempt=models.IntegerField()
    right=models.IntegerField()
    wrong=models.IntegerField()
    marks=models.IntegerField()
    score=models.IntegerField()
    test_id=models.IntegerField()
    branch=models.CharField(max_length=100)
    student_id=models.CharField(max_length=100)
