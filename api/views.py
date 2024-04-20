from django.shortcuts import render

from accounts.models import User, UserProfile
from .serializers import UserSerializer, ProfileSerializer
from rest_framework.viewsets import ModelViewSet


class UserViewSet(ModelViewSet):
                   serializer_class=UserSerializer
                   queryset=User.objects.all()


class ProfileViewSet(ModelViewSet):
                   serializer_class=ProfileSerializer
                   queryset=UserProfile.objects.all()
