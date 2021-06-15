from django.shortcuts import render
from .sz import GetBasicUserInfoSerializer,GetFullUserSerializer,UserSerializerWithToken
from rest_framework import generics,permissions,status

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser,FormParser
from .models import User,UserFollowing
from problem.sz import ProblemSerializer


@api_view(['GET'])
def get_current_user(request):
    serializer = GetFullUserSerializer(request.user)
    return Response(serializer.data)
# show user
class ShowUser(APIView):
    def get(self,request,pk):
        user = User.objects.get(id=pk)
        sz = GetFullUserSerializer(user,many=False)        
        savedProblem=ProblemSerializer(user.problemLikes.all(),many=True)        
        return Response({"user":sz.data,"savedProblems":savedProblem.data },status=status.HTTP_200_OK)

# show followings & followers 
class ShowFollow(APIView):
    def get(self,request,pk):
        user = User.objects.get(id=pk)
        followingUsers=user.following.all()
        following=[followingUser.following_user_id for followingUser in followingUsers]
        followingSz = GetBasicUserInfoSerializer(following,many=True)        

        followerUsers=user.followers.all()
        followers=[follower.user_id for follower in followerUsers]
        followersSz = GetBasicUserInfoSerializer(followers,many=True)   

        return Response({"following":followingSz.data,"followers":followersSz.data },status=status.HTTP_200_OK)

# check if the pass&email are valid
class CheckInfo(APIView):
        
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
class Follow(APIView):    
    def post(self,request):        
        user = User.objects.get(id=request.user.id)
        target = User.objects.get(id=request.data.get('target'))
        action=request.data.get("action")
        if action == "unfollow":
            UserFollowing.objects.get(user_id=user,following_user_id=target).delete()                
        else:
            UserFollowing.objects.create(user_id=user,following_user_id=target)                

        
        return Response(status=status.HTTP_200_OK)

