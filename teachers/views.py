from django.shortcuts import render, redirect
from django.http import Http404

from django.http import HttpResponse
from teachers.forms import TeacherFD
from teachers.models import Teacher

def teachers_page(request):
    teachers = Teacher.objects.all()
    return render(request, './teachers/teacher_list.html', context={'teachers': teachers})


def teacher_description(request, teacher_id):
    teacher = Teacher.objects.get(id=teacher_id)
    coursesy = teacher.courses.all()
    if request.method == 'POST':
        form = TeacherFD(request.POST)
        if form.is_valid():
            Teacher.objects.create(
                question=form.cleaned_data["question"],
            )
        return redirect('teachers')
    else:
        form = TeacherFD()
    if teacher is not None:
       return render(request, './teachers/teachers_info.html', context={'teacher': teacher, 'course': coursesy, 'form':form})

