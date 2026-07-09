from django.urls import path
from . import views

# Эта строчка обязательна для работы имен путей!
app_name = 'courses'

urlpatterns = [
    path('', views.CourseListView.as_view(), name='course_list'),
    path('<int:pk>/', views.CourseDetailView.as_view(), name='course_detail'),
]
