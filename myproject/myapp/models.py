from django.db import models

# Create your models here.
class Student(models.Model):
    studentId=models.IntegerField()
    studentName=models.CharField(max_length=24)
    studentRollNo=models.CharField(max_length=24)
    studentBranch=models.CharField(max_length=12,default="cse")


    def __str__(self):
      return self.studentName