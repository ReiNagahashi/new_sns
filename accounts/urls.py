from django.urls import path,include
from .views import *
from rest_framework import routers

urlpatterns = [
    path('current_user/',get_current_user),
    path('check_user/',CheckInfo.as_view()),
    path('<int:pk>',ShowUser.as_view()),    
    path('user/create',CreateUserView.as_view()),
    path('user/follow/',Follow.as_view()),
    path('user/followers/<int:pk>',ShowFollow.as_view()),
    path('profile/create/<int:pk>',CreateProfile.as_view()),
]