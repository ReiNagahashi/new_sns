from django.shortcuts import render
from .sz import FollowerTargetSerializer,GetFullUserSerializer,UserSerializerWithToken
from rest_framework import generics,permissions,status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser,FormParser
from django.contrib.auth.forms import AuthenticationForm
from .models import User
import datetime


@api_view(['GET'])
def get_current_user(request):
    serializer = GetFullUserSerializer(request.user)
    return Response(serializer.data)
# show user
class ShowUser(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = GetFullUserSerializer
    permission_classes = (permissions.AllowAny,)

# check if the pass&email are valid
class CheckInfo(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def post(self,request):
        try:        
            email = User.objects.get(email=request.data.get('user')['email'])
        except:email=None        
        if email:
            if email.check_password(request.data.get('user')['password']):            
                return Response({'response':'success','message':'User checked successfully'})

        return Response({'response':'error','message':'No data found'})


# Register
class CreateUserView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self,request):
        user = request.data.get('user')
        if not user:
            return Response({'response':'error','message':'No data found'})

        serializer = UserSerializerWithToken(data = user)

        if serializer.is_valid(): serializer.save()
        else: return Response({'response':'error','message':serializer.errors})

        return Response({'response':'success','message':'User created successfully'})

# create profile
class CreateProfile(generics.UpdateAPIView):
    parser_classes = [MultiPartParser,FormParser]

    def put(self,request,pk,format=None):
        user = User.objects.get(id=pk)
        sz = GetFullUserSerializer(instance=user,data=request.data)        
        if sz.is_valid():
            sz.save()
            return Response(sz.data,status=status.HTTP_200_OK)
        else:
            return Response(sz.errors,status=status.HTTP_400_BAD_REQUEST)
# Follow
class FollowUser(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self,request):                
        friendsSerializer = FollowerTargetSerializer(data=request.data)        
        if friendsSerializer.is_valid():
            target = User.objects.get(id=request.data["target"])
            friendsSerializer.save(follower=request.user,target=target)
            print(request.user)
            # follower = User.objects.get(id=request.data["follower"])
            # follower=request.data["follower"],target=request.data["target"]
            sz = GetFullUserSerializer(instance=request.user.data,data=friendsSerializer.data)        
            # follower.friends.add(friendsSerializer,through_defaults={'date':datetime.now()})            
            # print(friendsSerializer,sz)
            if sz.is_valid():             
                sz.save()            
                return Response(sz.data,status=status.HTTP_200_OK)
            else:
                return Response(sz.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(friendsSerializer.errors,status=status.HTTP_400_BAD_REQUEST)