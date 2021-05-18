from rest_framework import serializers as sz
from .models import *
from .models import User

class GetUserIdSerializer(sz.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',)
class FollowerTargetSerializer(sz.ModelSerializer):
    follower=GetUserIdSerializer(read_only=True,many=False)
    target=GetUserIdSerializer(read_only=True,many=False)
    class Meta:
        model = Follow
        fields = ('id','target','follower')
class GetFullUserSerializer(sz.ModelSerializer):
    friends = FollowerTargetSerializer(read_only=True,many=True,allow_null=True)
    class Meta:
        model = User
        fields = ('id','fullname','email','introduction','avatar','friends')

class UserSerializerWithToken(sz.ModelSerializer):
    password = sz.CharField(write_only=True)
    token = sz.SerializerMethodField()

    def get_token(self, object):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(object)
        token = jwt_encode_handler(payload)
        return token
    def create(self, validated_data):
        user = User.objects.create(
            email = validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    class Meta:
        model = User
        fields = ('token', 'email', 'password')
