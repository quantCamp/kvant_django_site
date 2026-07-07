from django.urls import path
from . import views
from teachers import views as teacher_views
# Имя приложения для обратного разрешения URL (namespace)
app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('teachers/', teacher_views.teachers_page, name='teachers_page'),
]
