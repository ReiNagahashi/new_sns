from django.urls import path
from .views import *

urlpatterns = [
    path('current_user/',get_current_user),
    path('check_user/',Check_info.as_view()),
    path('users/create',CreateUserView.as_view())
]