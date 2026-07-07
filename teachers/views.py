from django.shortcuts import render
from django.http import Http404

from django.http import HttpResponse

from teachers.models import Teacher

def teachers_page(request):

    teachers = Teacher.objects.all()

    return render(request, './teachers/teacher_list.html', context={
        'teachers': teachers
    })

# Create your views here.
def teacher_description(request, teacher_name, id):

    teacher = Teacher.objects.get(id = id)
    if teacher is not None:
        return render(request, './teacher.html', context={'teacher': teacher})

    raise Http404(f'Учителя {teacher_name} нет')

