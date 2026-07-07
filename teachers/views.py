from django.shortcuts import render
from teachers.models import Teacher
from courses.models import Course
# Create your views here.

def teachersi(request, id):
    teacher = Teacher.objects.get(id=id)
    return render(request, 'teacher_info.html', context={'teacher': teacher, 'course': coursesy})
    
