from django.contrib import admin

# Register your models here.


from QuestionBank.models import Subject, Question, QuestionBanks, Question_Answer, QuestionsSections, Answer, StudentResponse, StudentQuestionResponse

admin.site.register(Subject)
admin.site.register(Question)
admin.site.register(QuestionBanks)
admin.site.register(Question_Answer)
admin.site.register(QuestionsSections)
admin.site.register(Answer)
admin.site.register(StudentResponse)

admin.site.register(StudentQuestionResponse)


