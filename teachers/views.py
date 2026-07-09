from django.shortcuts import render, redirect
from django.http import Http404

from django.http import HttpResponse
from teachers.forms import TeacherFD
from teachers.models import Teacher, TeacherFeedBack

def teachers_page(request):
    teachers = Teacher.objects.all()
    return render(request, './teachers/teacher_list.html', context={'teachers': teachers})


def teacher_description(request, teacher_id):
    teacher = Teacher.objects.get(id=teacher_id)
    coursesy = teacher.courses.all()
    if request.method == 'POST':
        form = TeacherFD(request.POST)
        if form.is_valid():
            TeacherFeedBack.objects.create(
                teacher = teacher,
                question=form.cleaned_data["question"],
            )
        return redirect('teachers:teacher_name', teacher_id = teacher_id)
    else:
        form = TeacherFD()
    if teacher is not None:
       return render(request, './teachers/teachers_info.html', context={'teacher': teacher, 'courses': coursesy, 'form':form})

