from django.urls import path

from teachers import views

urlpatterns = [
    path('', views.teachers_page, name='teacher_page'),
    path('<int:teacher_id>/', views.teachersi, name='teacher_name')
]