from django.urls import path, include

from . import views
urlpatterns = [
                path('detail/<pk>', views.get_question_bank,name='question_list'),
                path('allquestion/answer/<pk>', views.get_all_question_answer,name='question_answer_list'),
                path('check/answers', views.check_question_answer,name='check_answers'),
                path('student/result', views.get_student_result,name='student_result'),
                path('allstudent/result', views.get_all_student_result,name='all_student_result'),
                path('students', views.get_all_student_list,name='all_student'),

                
]