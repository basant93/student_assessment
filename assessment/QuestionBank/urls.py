from django.urls import path, include

from . import views
urlpatterns = [
                path('detail/<pk>', views.get_question_bank,name='question_list'),
                

]