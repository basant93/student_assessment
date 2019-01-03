from django.db import models
from SchoolStudents.models import Grades, Sections, UserProfile
from django.contrib.auth.models import User, Group
from django.core.validators import RegexValidator
from assessment import constant

# Create your models here.

class Subject(models.Model):
    sub_name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.sub_name






class QuestionBanks(models.Model):
    ques_grades = models.OneToOneField(Grades,on_delete=models.PROTECT, blank=True, null=True)
    ques_sections = models.OneToOneField(Sections,on_delete=models.PROTECT, blank=True, null=True)
    total_marks = models.IntegerField(default=100, null=True)
    total_time = models.DateTimeField(blank= True)
    general_instructions = models.TextField(blank=True, null=True)
    ques_bank_title = models.CharField(max_length=200,  blank = True)
    subject = models.OneToOneField(Subject, on_delete=models.SET_NULL, blank = True, null=True)
    student_assigned_list = models.ManyToManyField(UserProfile, through='StudentResponse' )
    author = models.OneToOneField(User, on_delete=models.SET_NULL, blank=True,null=True )
    creation_date = models.DateField(auto_now_add=True, blank = True)
    exam_start_time = models.TimeField(blank = True, auto_now_add=True)
    exam_end_time = models.TimeField(blank = True, auto_now_add=True)

    def __str__(self):
        return self.ques_bank_title


class StudentResponse(models.Model):
    question_bank = models.ForeignKey(QuestionBanks, on_delete=models.CASCADE)
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    marks_scored = models.IntegerField(default=0, blank=True)
    is_present = models.BooleanField(default=False)

    def __str__(self):
        return self.question_bank + " - " + self.student.auth_user.username

class QuestionsSections(models.Model):
    section_name = models.CharField(max_length=200,  blank =True)
    comprehension_desc = models.TextField(blank=True)

    def __str__(self):
        return self.section_name 


class Question(models.Model):
    QUESTION_TYPE_CHOICES = (
        (constant.get_mcq_name(), 'Multiple Choice Question' ), (constant.get_true_or_false_name(), 'True/False' ), (constant.get_fill_in_the_blanks_name(), 'Fill in the blanks'), 
        (constant.get_match_the_following_name(), 'Match the Following'), (constant.get_comprehension_name(), 'Comprehension')
        )
    
    question_type = models.CharField(max_length=50, choices = QUESTION_TYPE_CHOICES, blank = False, unique = True)
    question_title = models.TextField(blank=False)
    question_marks = models.IntegerField(blank=False)
    section = models.ForeignKey(QuestionsSections, blank=True,  null=True,  on_delete= models.SET_NULL)

    def __str__(self):
        return self.question_title 

class Answer(models.Model):
    option_one = models.CharField(max_length=300, blank=False)
    option_two = models.CharField(max_length=300, blank= True, null=True)
    answers_marks = models.IntegerField(default=0, blank=False)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.option_one 

class Question_Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete = models.SET_NULL, blank = True, null=True)

    def __str__(self):
        return self.question.question_title


class StudentQuestionResponse(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete = models.SET_NULL, blank = True, null=True)

    def __str__(self):
        return self.question.question_title + " - " +self.answer.option_one








