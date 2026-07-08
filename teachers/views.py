from django.shortcuts import render
from django.http import Http404

from django.http import HttpResponse

from teachers.models import Teacher
from courses.models import Course
# Create your views here.

def teachers_page(request):
    teachers = Teacher.objects.all()
    return render(request, './teachers/teacher_list.html', context={'teachers': teachers})

# def teacher_description(request, teacher_name, id):
#     teacher = Teacher.objects.get(id = id)
#     if teacher is not None:
#         return render(request, './teacher.html', context={'teacher': teacher})

#     raise Http404(f'Учителя {teacher_name} нет')

def teachersi(request, teacher_id):
    teacher = Teacher.objects.get(id=teacher_id)
    coursesy = teacher.courses.all()
    return render(request, './teachers/teachers_info.html', context={'teacher': teacher, 'course': coursesy})
    
