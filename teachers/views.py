from django.shortcuts import render
from teachers.models import Teacher
# Create your views here.

def teachers(request, teach_name):
    teachery = 12