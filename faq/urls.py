from django.urls import path

from faq import views

urlpatterns = [
    path('', views.question),
]
