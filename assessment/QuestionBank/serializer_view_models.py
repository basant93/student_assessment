from rest_framework import serializers
from SchoolStudents.serializer_view_models import GradesMainSerializer, SectionMainSerializer

class SubjectMainSerializer(serializers.Serializer):
    sub_name = serializers.CharField()
    description = serializers.CharField()





class QuestionBankDetailMainSerializer(serializers.Serializer):

    ques_grades = GradesMainSerializer()
    ques_sections = SectionMainSerializer()
    total_marks = serializers.IntegerField()
    total_time = serializers.TimeField()
    general_instructions = serializers.CharField()
    ques_bank_title = serializers.CharField()
    subject = SubjectMainSerializer()





class QuestionBankMainSerializer(serializers.Serializer):

    success = serializers.BooleanField()
    error_code = serializers.IntegerField()
    status_code = serializers.CharField()
    data = QuestionBankDetailMainSerializer()
