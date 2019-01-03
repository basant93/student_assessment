from django.contrib import admin

# Register your models here.

from SchoolStudents.models import School, Sections, SchoolGradeDetails, UserProfile, StudentDetails, Grades

admin.site.register(UserProfile)
admin.site.register(Sections)
admin.site.register(SchoolGradeDetails)
admin.site.register(School)
admin.site.register(StudentDetails)
admin.site.register(Grades)
