from django.urls import path
from .views import *

urlpatterns = [
    path('current_user/',get_current_user),
    path('check_user/',CheckInfo.as_view()),
    path('<int:pk>',ShowUser.as_view()),    
    path('user/create',CreateUserView.as_view()),
    path('user/follow',FollowUser.as_view()),
    path('profile/create/<int:pk>',CreateProfile.as_view()),
]