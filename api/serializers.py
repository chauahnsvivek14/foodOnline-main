from rest_framework import serializers
from accounts.models import User, UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= ['first_name','last_name','username','email','phone_number']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields= ['user','profile_picture','cover_photo','address','country','state','city','pin_code','latitude','longitude']
