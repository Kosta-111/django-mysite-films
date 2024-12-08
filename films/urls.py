from django.urls import path
from films import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('create/', views.upload, name = 'create'),
    path('details/<int:id>', views.details),
    path('delete/<int:id>', views.delete, name = 'delete')
]