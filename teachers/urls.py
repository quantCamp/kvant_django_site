from django.urls import path

from teachers import views

urlpatterns = [
    path('teacher/<int:id>/', views.teacher_description, name='id')
]