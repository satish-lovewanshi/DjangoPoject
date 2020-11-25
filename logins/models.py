from django.db import models
from django.contrib.auth.models import AbstractUser

    
class Code(models.Model):
    code=models.CharField(max_length=100)
    def __str__(self):
        return self.code


class User(AbstractUser):
    is_student=models.BooleanField(default=False)
    is_teacher=models.BooleanField(default=False)
    profile_update=models.BooleanField(default=False)
    
class Branch(models.Model):
    branch=models.CharField(max_length=100)
    def __str__(self):
        return self.branch
    
class Year(models.Model):
    year=models.CharField(max_length=100)
    def __str__(self):
        return self.year


class Student(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    phone=models.CharField(max_length=50)
    college_code=models.ForeignKey(Code,on_delete=models.CASCADE,blank=True)
    roll_number=models.CharField(max_length=50)
    branch=models.ForeignKey(Branch,on_delete=models.CASCADE,blank=True)
    year=models.ForeignKey(Year,on_delete=models.CASCADE,blank=True)
    # profile_update=models.BooleanField(default=False)
    

class Teacher(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    phone=models.CharField(max_length=50)
    college_code=models.ForeignKey(Code,on_delete=models.CASCADE)
    branch=models.ForeignKey(Branch,on_delete=models.CASCADE)
    # pass_number=models.IntegerField(unique=True)
    
