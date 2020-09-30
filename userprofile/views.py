from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.parsers import JSONParser 
from rest_framework.decorators import api_view
import json

from .constant import Page
from .response import (
    response_userprofile_incomplete1, response_userprofile_incomplete2,
    response_userprofile_complete, response_settings    
)        

@api_view(['POST', 'GET'])
def userprofile_incomplete1(request):
    if request.method == 'GET':
        response = {
            Page.pg1.value : response_userprofile_incomplete1(Page.pg1.value),
        }
        return HttpResponse(json.dumps(response), content_type = 'application/json')
    else:
        return HttpResponse("false")

@api_view(['POST', 'GET'])
def userprofile_incomplete2(request):
    if request.method == 'GET':
        response = {
            Page.pg2.value : response_userprofile_incomplete2(Page.pg2.value),
        }
        return HttpResponse(json.dumps(response), content_type = 'application/json')
    else:
        return HttpResponse("false")

@api_view(['POST', 'GET'])
def userprofile_complete(request):
    if request.method == 'GET':
        response = {
            Page.pg3.value : response_userprofile_complete(Page.pg3.value),
        }
        return HttpResponse(json.dumps(response), content_type = 'application/json')
    else:
        return HttpResponse("false")

@api_view(['POST', 'GET'])
def settings(request):
    if request.method == 'GET':
        response = {
            Page.pg4.value : response_settings(Page.pg4.value),
        }
        return HttpResponse(json.dumps(response), content_type = 'application/json')
    else:
        return HttpResponse("false")
