from django.urls import path,include
from rest_framework import routers
from .views import UserViewSet, ProfileViewSet

router = routers.DefaultRouter()
router.register('user',UserViewSet, basename='user')
router.register('profile',ProfileViewSet, basename='profile')

urlpatterns = [
    path('', include(router.urls)),
]
