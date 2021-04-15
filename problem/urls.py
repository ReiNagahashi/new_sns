from django.urls import path
from . import views

urlpatterns = [
    path('',views.apiOverView,name='api-overview'),
    path('index',views.index,name='index'),
    path('create',views.create,name='create'),
    path('delete/<str:pk>',views.delete,name='delete'),
    path('single/<str:pk>',views.single,name='single'),
    path('update/<str:pk>',views.update,name='update')
]