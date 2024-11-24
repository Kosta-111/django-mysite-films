from django.urls import path
from films import views

urlpatterns = [
    path('home/', views.home),
    path('details/<int:id>', views.details),
    path('', views.home)
]