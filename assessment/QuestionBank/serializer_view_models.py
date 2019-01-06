from rest_framework import serializers
from SchoolStudents.serializer_view_models import GradesMainSerializer, SectionMainSerializer
from .serializer_db_models import AnswerMainSerializer


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


class AnswerWithIdSerializer(serializers.Serializer):
    answer_id = serializers.IntegerField()
    option_one = serializers.CharField()
    option_two = serializers.CharField()
    answers_marks = serializers.IntegerField()
    is_correct = serializers.BooleanField()


class SectionQuesAnsSerializer(serializers.Serializer):
    question_id = serializers.IntegerField()
    question_type = serializers.CharField()
    question_title = serializers.CharField()
    question_marks = serializers.IntegerField()
    question_answer_options = AnswerWithIdSerializer(many=True)

class SectionQuestionInfoSerializer(serializers.Serializer):

    section_questions_info = SectionQuesAnsSerializer(many = True)

class SectionInfoSerializer(serializers.Serializer):

    section_name = serializers.CharField()
    comprehension_description = serializers.CharField()
    question_answer_list = SectionQuestionInfoSerializer()

    #many=True


class QuestionBankInfoSerializer(serializers.Serializer):

    ques_bank_id = serializers.IntegerField()
    ques_bank_title = serializers.CharField()
    exam_start_time = serializers.TimeField()
    exam_end_time = serializers.TimeField()
    subject = SubjectMainSerializer()
    general_instruction = serializers.CharField()
    section_info = SectionInfoSerializer(many=True)




class QuestionAnswerMainSerializer(serializers.Serializer):

    success = serializers.BooleanField()
    error_code = serializers.IntegerField()
    status_code = serializers.CharField()
    data = QuestionBankInfoSerializer()


class StudentResponseMessageSerializer(serializers.Serializer):
    message = serializers.CharField()


class StudentResponserMainSerializer(serializers.Serializer):

    success = serializers.BooleanField()
    error_code = serializers.IntegerField()
    status_code = serializers.CharField()
    data = StudentResponseMessageSerializer()


class StudentMarksInfoSerializer(serializers.Serializer):
    question_bank_title = serializers.CharField()
    user_name = serializers.CharField()
    user_email = serializers.EmailField()
    marks_scored = serializers.IntegerField()


class StudentMarksMainSerializer(serializers.Serializer):

    success = serializers.BooleanField()
    error_code = serializers.IntegerField()
    status_code = serializers.CharField()
    data = StudentMarksInfoSerializer()

class AllStudentMarksDetailResponse(serializers.Serializer):
    question_bank_title = serializers.CharField()
    user_name = serializers.CharField()
    user_email = serializers.EmailField()
    marks_scored = serializers.IntegerField()


class AllStudentMarksInfoResponse(serializers.Serializer):
    
    student_list = AllStudentMarksDetailResponse(many=True)


class AllStudentMarksMainSerializer(serializers.Serializer):

    success = serializers.BooleanField()
    error_code = serializers.IntegerField()
    status_code = serializers.CharField()
    data = AllStudentMarksInfoResponse()