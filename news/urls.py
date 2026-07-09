from django.urls import path, include
from . import views

# Имя приложения для обратного разрешения URL (namespace)
app_name = 'news'

urlpatterns = [
    path('', views.news_list , name='index'),
    path('detail/<int:news_id>', views.news_detail , name='detail'),
    path('add/', views.news_add, name='add')
]

