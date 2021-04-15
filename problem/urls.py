from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverView,name="api-overview"),
    path('index', views.index,name="problem_list"),
    path('detail/<str:pk>',views.single,name="problem_single"),
    path('create',views.create,name="problem_create"),
    path('update/<str:pk>',views.update,name="problem_update"),
    path('delete/<str:pk>',views.delete,name="problem_delete"),
]