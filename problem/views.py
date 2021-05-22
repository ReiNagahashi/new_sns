from django.shortcuts import render
from .sz import ProblemSerializer,ProblemLikeSerializer,BasicProblemSerializer
from accounts.sz import GetFullUserSerializer as GS
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics,permissions,status
from rest_framework.parsers import MultiPartParser,FormParser
from .models import Problem

class ViewProblem(generics.ListCreateAPIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
    permission_classes = (permissions.AllowAny,)

class ShowProblem(generics.RetrieveAPIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
    permission_classes = (permissions.AllowAny,)

class CreateProblem(APIView):
    parser_classes = [MultiPartParser,FormParser]

    def post(self,request,format=None):        
        sz = ProblemSerializer(data=request.data)                  
        if sz.is_valid():            
            sz.save(author=request.user)
            return Response(sz.data,status=status.HTTP_200_OK)
        else:
            return Response(sz.errors,status=status.HTTP_400_BAD_REQUEST)

class EditProblem(generics.RetrieveAPIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer

class UpdateProblem(generics.UpdateAPIView):
    parser_classes = [MultiPartParser,FormParser]

    def put(self,request,pk,format=None):
        problem = Problem.objects.get(id=pk)        
        sz = ProblemSerializer(instance=problem,data=request.data)


        if sz.is_valid():
            sz.save()
            return Response(sz.data,status=status.HTTP_200_OK)
        else:
            return Response(sz.errors,status=status.HTTP_400_BAD_REQUEST)

class DeleteProblem(generics.DestroyAPIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer

# Like problem
class LikeProblem(APIView):    
    def post(self,request):        
        problem = Problem.objects.get(id=request.data)            
        if request.user in problem.likes.all():
            problem.likes.remove(request.user)
        else:
            problem.likes.add(request.user)
        return Response(status=status.HTTP_200_OK)