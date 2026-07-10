from django.urls import path, include
from . import views
# Имя приложения для обратного разрешения URL (namespace)
app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    
]
