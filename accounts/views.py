from django.shortcuts import render
from .sz import *
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


@api_view(['GET'])
def get_current_user(request):
    serializer = GetFullUserSerializer(request.user)
    return Response(serializer.data)

class Check_info(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self,request):
        try:        
            user = User.objects.get(username=request.data.get('user')['username'])
        except:user=None        
        if user:
            if user.check_password(request.data.get('user')['password']):            
                return Response({'response':'success','message':'User checked successfully'})

        return Response({'response':'error','message':'No data found'})


# レジスター機能
class CreateUserView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self,request):
        user = request.data.get('user')
        if not user:
            return Response({'response':'error','message':'No data found'})
        
        serializer = UserSerializerWithToken(data = user)

        if serializer.is_valid(): saved_user = serializer.save()
        else: return Response({'response':'error','message':serializer.errors})

        return Response({'response':'success','message':'User created successfully'})

