from library import views

from django.urls import path

urlpatterns = [
    path('', views.main_page),
    path('<int:category>/', views.category_page),
]
