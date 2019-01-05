from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from .view_models import QuestionBankResponse, QuestionBankDataResponse
from QuestionBank.models import QuestionBanks
from .serializer_view_models import QuestionBankMainSerializer


@api_view(['GET'])
def get_question_bank(request,pk):
    try:
        # If exception is not thrown, username already exists.
        ques_bank_obj = QuestionBanks.objects.get(id=pk)
    except ObjectDoesNotExist:
        ques_bank_obj = None
    
    main_response = QuestionBankResponse()
    main_response.success = True
    main_response.error_code = 0
    main_response.status_code = status.HTTP_200_OK
    main_response.data = QuestionBankDataResponse(ques_bank_obj)
    serializer = QuestionBankMainSerializer(main_response)

    return Response(serializer.data)
    

