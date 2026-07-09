from library import views
from django.urls import path

app_name = 'library'

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('<int:category_id>/', views.category_page, name='category_page'),
]
