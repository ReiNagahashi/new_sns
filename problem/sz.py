from rest_framework import serializers
from .models import Problem,ProblemLike
from accounts.sz import GetFullUserSerializer

class ProblemLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProblemLike
        fields = ('id',)

class BasicProblemSerializer(serializers.ModelSerializer):
    likes=ProblemLikeSerializer(read_only=True,many=True)
    class Meta:
        model = Problem
        fields = ('id','likes')


class ProblemSerializer(serializers.ModelSerializer):
    likes = ProblemLikeSerializer(read_only=True,many=True)
    author = GetFullUserSerializer(read_only=True,many=False)

    class Meta:
        model = Problem
        fields = ('id','title','description','thumb','author','video','likes')

