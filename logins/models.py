from django.db import models

# Create your models here.
class Branch(models.Model):
    branch=models.CharField(max_length=100)
    def __str__(self):
        return self.branch
    
class Year(models.Model):
    year=models.CharField(max_length=100)
    def __str__(self):
        return self.year
    
class Code(models.Model):
    code=models.CharField(max_length=100)
    def __str__(self):
        return self.code
    
class StudentReg(models.Model):
    college_code=models.ForeignKey(Code,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    roll_number=models.CharField(max_length=100)
    branch=models.ForeignKey(Branch,on_delete=models.CASCADE)
    year=models.ForeignKey(Year,on_delete=models.CASCADE)
    mobile=models.IntegerField(unique=True)
class TeacherReg(models.Model):
    college_code=models.ForeignKey(Code,on_delete=models.CASCADE)
    branch=models.ForeignKey(Branch,on_delete=models.CASCADE)
    pass_number=models.IntegerField(unique=True)
    name=models.CharField(max_length=200)
    mobile=models.IntegerField(unique=True)
    
