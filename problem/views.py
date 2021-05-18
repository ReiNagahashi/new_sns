from django.shortcuts import render
from .sz import ProblemSerializer as PS
from accounts.sz import GetFullUserSerializer as GS
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics,permissions,status
from rest_framework.parsers import MultiPartParser,FormParser
from .models import Problem

class ViewProblem(generics.ListCreateAPIView):
    queryset = Problem.objects.all()
    serializer_class = PS
    permission_classes = (permissions.AllowAny,)

class ShowProblem(generics.RetrieveAPIView):
    queryset = Problem.objects.all()
    serializer_class = PS
    permission_classes = (permissions.AllowAny,)

class CreateProblem(APIView):
    parser_classes = [MultiPartParser,FormParser]

    def post(self,request,format=None):        
        sz = PS(data=request.data)                  
        if sz.is_valid():            
            sz.save(author=request.user)
            return Response(sz.data,status=status.HTTP_200_OK)
        else:
            return Response(sz.errors,status=status.HTTP_400_BAD_REQUEST)

class EditProblem(generics.RetrieveAPIView):
    queryset = Problem.objects.all()
    serializer_class = PS

class UpdateProblem(generics.UpdateAPIView):
    parser_classes = [MultiPartParser,FormParser]

    def put(self,request,pk,format=None):
        problem = Problem.objects.get(id=pk)        
        sz = PS(instance=problem,data=request.data)


        if sz.is_valid():
            sz.save()
            return Response(sz.data,status=status.HTTP_200_OK)
        else:
            return Response(sz.errors,status=status.HTTP_400_BAD_REQUEST)

class DeleteProblem(generics.DestroyAPIView):
    queryset = Problem.objects.all()
    serializer_class = PS
