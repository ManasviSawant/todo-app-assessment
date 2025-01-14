# tasks/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('mark/<int:task_id>/', views.mark_task_complete, name='mark_task_complete'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('add/', views.add_task, name='add_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
]
