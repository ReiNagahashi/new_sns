from rest_framework import serializers
from .models import Problem
from accounts.sz import GetFullUserSerializer

class ProblemSerializer(serializers.ModelSerializer):
    author = GetFullUserSerializer(read_only=True,many=False)

    class Meta:
        model = Problem
        fields = ('id','title','description','thumb','author','video')
