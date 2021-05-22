from django.urls import path
from .views import *

urlpatterns = [
    path('',ViewProblem.as_view()),
    path('<int:pk>',ShowProblem.as_view()),
    path('create/',CreateProblem.as_view()),
    path('edit/<int:pk>',EditProblem.as_view()),
    path('update/<int:pk>',UpdateProblem.as_view()),
    path('delete/<int:pk>',DeleteProblem.as_view()),
    # like
    path('like/',LikeProblem.as_view())
]