from django.urls import path
from . import views

# Имя приложения для обратного разрешения URL (namespace)
app_name = 'about'

urlpatterns = [
    path('about', views.about_page, name='about'),
]
