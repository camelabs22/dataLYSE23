from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .serializer import DatalyseSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 


@api_view(['POST'])
def sign_up(self, request):
    datas_serialized = DatalyseSerializer(data = request.data)
    if datas_serialized.is_valid(raise_exception=True):
        datas_serialized.save()
        return Response(status = status.HTTP_201_CREATED)

@api_view(['GET'])
def sign_in(self, request):
    datas = Users.objects.all()
    datas_serialized = DatalyseSerializer(datas, many = True)
    return Response(datas_serialized)

@api_view(['GET'])
def display(request, email):
    try:
        datas = User_datasets.objects.get(pk=email)
    except User_datasets.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    datasets_serialized = DatalyseSerializer(datas, many = True)
    return Response(datasets_serialized)



