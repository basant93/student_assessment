from django.db import models
from SchoolStudents.models import Grades, Sections, Student
from django.contrib.auth.models import User


# Create your models here.

class Subject(models.Model):
    sub_name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)


class StudentResponse(models.Model):
    question_bank = models.ForeignKey(QuestionBanks, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    marks_scored = models.IntegerField(default=0, blank=True)
    is_present = models.BooleanField(default=False)


class QuestionBanks(models.Model):
    ques_grades = models.OneToOneField(Grades,on_delete=models.PROTECT, blank=True, null=True)
    ques_sections = models.OneToOneField(Sections,on_delete=models.PROTECT, blank=True, null=True)
    total_marks = models.IntegerField(default=100, null=True)
    total_time = models.DateTimeField(blank= True)
    general_instructions = models.TextField(blank=True, null=True)
    ques_bank_title = models.CharField(blank = True)
    subject = models.OneToOneField(Subject, on_delete=models.SET_NULL, blank = True, null=True)
    student_assigned_list = models.ManyToManyField(Student, through=StudentResponse)
    author = models.OneToOneField(User, on_delete=models.SET_NULL, blank=True,null=True )
    creation_date = models.DateField(auto_now_add=True, blank = True)
    exam_start_time = models.TimeField(blank = True, auto_now_add=True)
    exam_end_time = models.TimeField(blank = True, auto_now_add=True)


class StudentPresence(models.Model):
    ques_bank = 






