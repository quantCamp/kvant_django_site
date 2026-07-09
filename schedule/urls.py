from django.urls import path

from schedule import views

urlpatterns = [
    path('', views.schedule_view),
    path('<int:pk>/', views.schedule_detail)
]