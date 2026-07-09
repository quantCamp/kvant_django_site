from django.urls import path

from teachers import views

urlpatterns = [

    path('', views.teachers_page, name='teachers_page'),
    path('<int:teacher_id>/', views.teacher_description, name='teacher_name')
]