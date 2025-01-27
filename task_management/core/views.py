from django.shortcuts import render
from .models import User, Project, Category, Priority, Task
from .serializers import UserSerializer, ProjectSerializer, CategorySerializer, PrioritySerializer, TaskSerializer
from rest_framework import permissions, viewsets

# Create your views here.

