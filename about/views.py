from django.shortcuts import render, redirect
from about.forms import SchoolApplicationForm
from about.models import SchoolApplication
from django.contrib import messages

# Create your views here.

def about_page(request):
    if request.method == 'POST':
        form = SchoolApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            SchoolApplication.objects.create(
                parent_name=form.cleaned_data["parent_name"],
                student_name=form.cleaned_data["student_name"],
                student_age=form.cleaned_data["student_age"],
                phone=form.cleaned_data["phone"],
                email=form.cleaned_data["email"],
                achievements=form.cleaned_data["achievements"]
            )
            messages.success(request, 'Регистрация прошла успешно!')
        return redirect('/about')
    else:
        form = SchoolApplicationForm()

    return render(request, 'about/about.html', context={"form": form})