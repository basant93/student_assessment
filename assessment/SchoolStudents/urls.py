from django.urls import path, include

from . import views
urlpatterns = [
                path('student/<pk>', views.get_student_info,name='question_list'),
                

]