from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.parsers import JSONParser 
from rest_framework.decorators import api_view
import json

from .constant import Page
from .response import (
    response_advance_filter, response_filter, 
    response_subscribe_elite, response_elite_register1, response_elite_register2,
    response_elite_register3, response_elite_register4, response_elite_register5,
    response_elite_payment, response_profile_card
)        

@api_view(['POST', 'GET'])
def advanceFilter(request):
    if request.method == 'GET':
        response = {
            Page.pg1.value : response_advance_filter(Page.pg1.value),
        }
        return HttpResponse(json.dumps(response), content_type = 'application/json')
    else:
        return HttpResponse("false")


@api_view(['POST', 'GET'])
def Filter(request):
    if request.method == 'GET':
        response = {
            Page.pg2.value : response_filter(Page.pg2.value),
        }
        return HttpResponse(json.dumps(response), content_type = 'application/json')
    else:
        return HttpResponse("false")


@api_view(['POST', 'GET'])
def suscribeElite(request):
    if request.method == 'GET':
        response = {
            Page.pg3.value : response_subscribe_elite(Page.pg3.value),
        }
        return HttpResponse(json.dumps(response), content_type = 'application/json')
    else:
        return HttpResponse("false")

@api_view(['POST', 'GET'])
def elite_register1(request):
    if request.method == 'GET':
        response = {
            Page.pg4.value : response_elite_register1(Page.pg4.value),
        }
        return HttpResponse(json.dumps(response), content_type = 'application/json')
    else:
        return HttpResponse("false")

@api_view(['POST', 'GET'])
def elite_register2(request):
    if request.method == 'GET':
        response = {
            Page.pg5.value : response_elite_register2(Page.pg5.value),
        }
        return HttpResponse(json.dumps(response), content_type = 'application/json')
    else:
        return HttpResponse("false")

@api_view(['POST', 'GET'])
def elite_register3(request):
    if request.method == 'GET':
        response = {
            Page.pg6.value : response_elite_register3(Page.pg6.value),
        }
        return HttpResponse(json.dumps(response), content_type = 'application/json')
    else:
        return HttpResponse("false")

@api_view(['POST', 'GET'])
def elite_register4(request):
    if request.method == 'GET':
        response = {
            Page.pg7.value : response_elite_register4(Page.pg7.value),
        }
        return HttpResponse(json.dumps(response), content_type = 'application/json')
    else:
        return HttpResponse("false")

@api_view(['POST', 'GET'])
def elite_register5(request):
    if request.method == 'GET':
        response = {
            Page.pg8.value : response_elite_register5(Page.pg8.value),
        }
        return HttpResponse(json.dumps(response), content_type = 'application/json')
    else:
        return HttpResponse("false")

@api_view(['POST', 'GET'])
def elite_payment(request):
    if request.method == 'GET':
        response = {
            Page.pg9.value : response_elite_payment(Page.pg9.value),
        }
        return HttpResponse(json.dumps(response), content_type = 'application/json')
    else:
        return HttpResponse("false")

@api_view(['POST', 'GET'])
def home(request):
    if request.method == 'GET':
        response = {
            Page.pg10.value : response_profile_card(Page.pg10.value),
        }
        return HttpResponse(json.dumps(response), content_type = 'application/json')
    else:
        return HttpResponse("false")




