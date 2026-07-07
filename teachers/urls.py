from django.urls import path

from teachers import views

urlpatterns = [
    path('teacher/<str:teacher_name>/', views.teacher_description, name='teacher_name')
]