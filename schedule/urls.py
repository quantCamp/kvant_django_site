from django.urls import path

from schedule import views

app_name = 'schedule'

urlpatterns = [
    path('', views.schedule_view, name='schedule_view'),
    path('<int:pk>/', views.schedule_detail, name='schedule_detail')
]