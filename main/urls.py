from django.urls import path
from . import views

# Имя приложения для обратного разрешения URL (namespace)
app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
]
