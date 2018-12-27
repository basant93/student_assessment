from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from .view_model import StudentProfileResponse, StudentProfileDataResponse
from .serializer_view_models import StudentProfileMainSerializer


@api_view(['GET'])
def get_student_info(request, pk):
    
    try:
        # If exception is not thrown, username already exists.
        user_obj = User.objects.get(id=pk)
    except ObjectDoesNotExist:
        user_obj = None
    
    main_response = StudentProfileResponse()
    main_response.success = True
    main_response.error_code = 0
    main_response.status_code = status.HTTP_200_OK
    main_response.data = StudentProfileDataResponse(user_obj)
    serializer = StudentProfileMainSerializer(main_response)

    return Response(serializer.data)

    

