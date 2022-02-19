from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('addTask/', views.addTask),
    path('deleteTask/<task_name>/', views.deleteTask),

    path('editTask/<task_name>/', views.editTask),
    path('editingTask/', views.editingTask),

    path('done/<task_name>/', views.done),
]