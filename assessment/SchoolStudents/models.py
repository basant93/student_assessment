from django.db import models
from django.contrib.auth.models import User, Group
from django.core.validators import RegexValidator
import datetime
from assessment import constant
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.db import transaction

# Create your models here.
class UserProfile(models.Model):
    contact_regex = RegexValidator(regex=r'[789]\d{9}$', message="Phone number is not valid.")
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others')
    )

    auth_user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_contact_no = models.CharField(validators=[contact_regex], max_length = 10 , blank=True, null= True)
    user_pincode = models.CharField(max_length = 6, blank = True, null=True)
    user_profile_image_url = models.URLField(null=True, blank=True)
    user_gender = models.CharField(max_length=6, choices = GENDER_CHOICES, blank= True, null= True)
    user_group = models.OneToOneField(Group ,null= True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.auth_user.username


class Grades(models.Model):
    GRADE_CHOICES = (
        ('Class 1', '1'), ('Class 2', '2'), ('Class 3', '3'), ('Class 4', '4'), 
        ('Class 5', '5'), ('Class 6', '6'), ('Class 7', '7'), ('Class 8', '8'),
        ('Class 9', '9'), ('Class 10', '10'), ('Class 11', '11'), ('Class 12', '12')
        )
    
    grade_name = models.CharField(max_length=10, choices = GRADE_CHOICES, blank = False, unique = True)



    def __str__(self):
        return self.grade_name

class Sections(models.Model):
    GRADE_CHOICES = (
        ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'),
        ('G', 'G'), ('H', 'H'),('Class I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L'),
        ('M', 'M'), ('N', 'N'), ('O', 'O'), ('P', 'P'), ('Q', 'Q'), ('R', 'R'),
        ('S', 'S'), ('T', 'T'),('U', 'U'), ('V', 'V'), ('W', 'W'), ('X', 'X'),
        ('Y', 'Y'), ('Z', 'Z')
        )
    grade_name = models.CharField(max_length=10, choices = GRADE_CHOICES, blank = False, unique = True)

    def __str__(self):
        return self.grade_name

class School(models.Model):
    school_contact_regex = RegexValidator(regex=r'[789]\d{9}$', message="Please enter valid phone number.")

    school_name = models.CharField(max_length = 200, blank = False)
    school_address = models.CharField(max_length = 500, blank = False)
    school_pincode = models.CharField(max_length = 6, blank = True, null=True)
    school_contact_no = models.CharField(validators=[school_contact_regex], max_length = 10 , blank=True, null= True)

    def __str__(self):
        return self.school_name



class StudentDetails(models.Model):
    YEAR_CHOICES = []
    for r in range(1980, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r,r))
    sd_grades = models.ForeignKey(Grades, on_delete= models.SET_NULL, null = True, blank=False)
    sd_sections = models.ForeignKey(Sections, on_delete= models.SET_NULL, null = True, blank=False)
    sd_academic_year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    student_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    school_profile_id = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.school_profile_id.school_name + " - " + self.student_profile_id.auth_user.username



class SchoolGradeDetails(models.Model):
    grades_id = models.ForeignKey(Grades, on_delete= models.SET_NULL, null = True)
    sections_id = models.ForeignKey(Sections, on_delete= models.SET_NULL, null = True)
    school_id = models.ForeignKey(School, on_delete= models.CASCADE)

    class Meta:
        unique_together = ('grades_id', 'sections_id', 'school_id')

    def __str__(self):
        return self.school_id.school_name + " - " + self.grades_id.grade_name + " - " + self.sections_id.grade_name


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def add_user_profile(sender, instance=None, **kwargs):
    """
    add user profile on addition of new User.
    """
    
    user_obj = User.objects.get(id= instance.id)
    # gr = Group.objects.get(name = constant.get_student_group_name())

    # UserProfile.objects.get_or_create(auth_user=user_obj, user_group=gr)

    # prof = UserProfile(auth_user=user_obj)
    # gr = Group.objects.get(name = constant.get_student_group_name())
    # prof.user_group = gr
    # try:
    #     prof.save()
    # except:
    #     print("User profile saved failed")

    try:
        # Duplicates should be prevented.
        with transaction.atomic():
            prof = UserProfile(auth_user=user_obj)
            gr = Group.objects.get(name = constant.get_student_group_name())
            prof.user_group = gr
            prof.save()
        
    except:
        pass

    
   
  
    


