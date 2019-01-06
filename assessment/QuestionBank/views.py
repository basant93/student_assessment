from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from SchoolStudents.models import UserProfile, Grades, Sections, School, StudentDetails
from .view_models import AssignmentMainResponse, QuestionBankDataResponse, QuestionAnswerDataResponse, StudentResponseSaved, StudentMarksResponse, AllStudentMarksMainResponse
from QuestionBank.models import QuestionBanks, Question_Answer, Question, Answer, StudentResponse
from .serializer_view_models import QuestionBankMainSerializer, QuestionAnswerMainSerializer, StudentResponserMainSerializer, StudentMarksMainSerializer, AllStudentMarksMainSerializer




@api_view(['GET'])
def get_question_bank(request,pk):
    try:
        # If exception is not thrown, username already exists.
        ques_bank_obj = QuestionBanks.objects.get(id=pk)
    except ObjectDoesNotExist:
        ques_bank_obj = None
    
    main_response = AssignmentMainResponse()
    main_response.success = True
    main_response.error_code = 0
    main_response.status_code = status.HTTP_200_OK
    main_response.data = QuestionBankDataResponse(ques_bank_obj)
    serializer = QuestionBankMainSerializer(main_response)

    return Response(serializer.data)
    

@api_view(['GET'])
def get_all_question_answer(request,pk):

    #request_data = JSONParser().parse(request)
    
    try:
        # If exception is not thrown, username already exists.
        ques_bank_obj = QuestionBanks.objects.get(id=pk)
    except ObjectDoesNotExist:
        ques_bank_obj = None
    
    main_response = AssignmentMainResponse()
    main_response.success = True
    main_response.error_code = 0
    main_response.status_code = status.HTTP_200_OK
    main_response.data = QuestionAnswerDataResponse(ques_bank_obj)
    serializer = QuestionAnswerMainSerializer(main_response)

    return Response(serializer.data)


@api_view(['POST'])
def check_question_answer(request):

    request_data = JSONParser().parse(request)

    question_answer_list = request_data['question_answer_list']
    user_obj = User.objects.get(id = request_data['user_id'])
    student_response_answer = []
    for ques  in question_answer_list:
        question_id = ques['question_id']
        for ans in ques['answers']:
            ques_obj = Question.objects.get(id = question_id)
            ans_obj = Answer.objects.get(id = ans['answer_id'])
            student_response_answer.append(ans_obj)
            
            ques_ans_obj = Question_Answer(question = ques_obj, answer = ans_obj, auth_user_id = user_obj.id )
            ques_ans_obj.save()

    marks_scored = 0
    user_profile_obj = UserProfile.objects.get(auth_user = user_obj)
    for answer in student_response_answer:
        if(answer.is_correct):
            marks_scored += answer.answers_marks
    question_bank_obj = QuestionBanks.objects.get(id = request_data['question_bank_id'])

    student_response = StudentResponse(question_bank = question_bank_obj, student = user_profile_obj, marks_scored = marks_scored, is_present = True)
    student_response.save()


   
    message = "Student response has been saved successfully."
    
    main_response = AssignmentMainResponse()
    main_response.success = True
    main_response.error_code = 0
    main_response.status_code = status.HTTP_200_OK
    main_response.data = StudentResponseSaved(message)
    serializer = StudentResponserMainSerializer(main_response)

    return Response(serializer.data)




@api_view(['POST'])
def get_student_result(request):

    request_data = JSONParser().parse(request)

    user_obj = User.objects.get(id = request_data['student_id'])
    user_profile_obj = UserProfile.objects.get(auth_user = user_obj)
    try:
        ques_bank_obj = QuestionBanks.objects.get(id= request_data['question_bank_id'])
        
    except ObjectDoesNotExist:
        ques_bank_obj = None
    
    student_response = StudentResponse.objects.filter( question_bank = ques_bank_obj, student = user_profile_obj ).first() 
    
    
    main_response = AssignmentMainResponse()
    main_response.success = True
    main_response.error_code = 0
    main_response.status_code = status.HTTP_200_OK
    main_response.data = StudentMarksResponse(student_response)
    serializer = StudentMarksMainSerializer(main_response)

    return Response(serializer.data)



@api_view(['POST'])
def get_all_student_result(request):

    request_data = JSONParser().parse(request)


    try:
        ques_bank_obj = QuestionBanks.objects.get(id= request_data['question_bank_id'])
        
    except ObjectDoesNotExist:
        ques_bank_obj = None
    
    student_response = StudentResponse.objects.filter( question_bank = ques_bank_obj ) 
    
    
    main_response = AssignmentMainResponse()
    main_response.success = True
    main_response.error_code = 0
    main_response.status_code = status.HTTP_200_OK
    main_response.data = AllStudentMarksMainResponse(student_response)
    serializer = AllStudentMarksMainSerializer(main_response)

    return Response(serializer.data)




@api_view(['POST'])
def get_all_student_list(request):

    request_data = JSONParser().parse(request)

    try:
        if(request_data['grade'] is not '' and request_data['section'] is not '' and request_data['school_id'] is not ''):
            grades = Grades.objects.filter(grade_name = request_data['grade']).first()
            sections = Sections.objects.filter(grade_name = request_data['section']).first()
            school = School.objects.filter(id = request_data['school_id']).first()

            student_details = list(StudentDetails.objects.filter(sd_grades = grades, sd_sections=sections, school_profile_id=school))

            student_details_list = []

            for student in student_details:
                student_details_list.append(student.student_profile)
        question_bank = QuestionBanks.objects.get(id = request_data['question_bank_id'])

    except ObjectDoesNotExist:
        student_details_list = None
        question_bank = None
    
    

    for profile in request_data['student_list']:
        user_obj = User.objects.get(id = profile['id'])
        user_profile_obj = UserProfile.objects.get(auth_user = user_obj)
        student_details_list.append(user_profile_obj)
        student_response = StudentResponse(question_bank = question_bank , student = user_profile_obj , marks_scored = 0 , is_present = False)
        student_response.save()
    

    message = "Student has been assigned the test successfully."

    main_response = AssignmentMainResponse()
    main_response.success = True
    main_response.error_code = 0
    main_response.status_code = status.HTTP_200_OK
    main_response.data = StudentResponseSaved(message)
    serializer = StudentResponserMainSerializer(main_response)

    return Response(serializer.data)




