from django.urls import path
from challenge.api.views import ListTodo, DetailTodo

urlpatterns = [
    path('List/', ListTodo.as_view()),
    path('<int:pk>/', DetailTodo.as_view()),
]