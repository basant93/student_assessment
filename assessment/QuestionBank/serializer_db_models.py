from rest_framework import serializers
from .models import Answer

class AnswerMainSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Answer
        fields = ('option_one', 'option_two', 'answers_marks', 'is_correct')
