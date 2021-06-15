from django.db.models import fields
from rest_framework import serializers as sz
from .models import User,UserFollowing

class FollowingSerializer(sz.ModelSerializer):

    class Meta:
        model = UserFollowing
        fields = ("id","following_user_id","timestamp")

class FollowersSerializer(sz.ModelSerializer):

    class Meta:
        model = UserFollowing
        fields = ("id","user_id","timestamp")

class GetBasicUserInfoSerializer(sz.ModelSerializer):
    class Meta:
        model=User
        fields=("id","fullname","avatar","introduction")

class GetFullUserSerializer(sz.ModelSerializer):
    following = sz.SerializerMethodField()
    followers = sz.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id','fullname','email','introduction','avatar','following','followers')
    
    def get_following(self,obj):
        return FollowingSerializer(obj.following.all(),many=True).data
    
    def get_followers(self,obj):
        return FollowersSerializer(obj.followers.all(),many=True).data

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
