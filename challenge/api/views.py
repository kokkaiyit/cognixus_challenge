from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from challenge.api.serializers import UserSerializer, GroupSerializer

from rest_framework import generics
from challenge.todo_list import models
from challenge.api.serializers import TodoSerializer
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class ListTodo(generics.ListCreateAPIView):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]
        
class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]
