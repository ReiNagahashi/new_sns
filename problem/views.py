from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from .sz import ProblemSerializer as PS
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Problem
# Create your views here.

@api_view(['GET'])
def apiOverView(request):
    api_urls = {
        'Index':'/index',
        'Detail':'/detail/<str:pk>',
        'Create':'/create',
        'Update':'/update/<str:pk>',
        'Delete':'/delete/<str:pk>',
    }
    return Response(api_urls)

@api_view(['GET'])
def index(request):
    problems = Problem.objects.all()
    sz = PS(problems,many=True)
    return Response(sz.data)

@api_view(['GET'])
def single(request,pk):
    problem = Problem.objects.get(id=pk)
    sz = PK(problems,many=False)

    return Response(sz.data)

@api_view(['POST'])
def create(request):
    request.data.author=request.user
    print(request.data,type(request.data))
    sz = PS(data=request.data)

    if sz.is_valid():
        print("OK")
        sz.save()
        
    return Response(sz.data)

@api_view(['PUT'])
def update(request,pk):
    problem = Problem.objects.get(id=pk)
    sz = PS(instance=problem,data=request.data)

    if sz.is_valid():sz.save()

    return Response(sz.data)

@api_view(['DELETE'])
def delete(request,pk):
    problem = Problem.objects.get(id=pk)
    problem.delete()

    return Response("Deleted Successfully")

