from django.urls import path, re_path
from main import views

urlpatterns = [
    path('todos/', views.toDoReturn, name = 'task_list'),
    path('todos/new/', views.newTask),
    path('todos/completed', views.toReturnCompleted, name = 'return_compl'),
    re_path(r'^todos/(\d+)/changed/', views.toChange, name='task_change'),
    re_path(r'^todos/(\d+)/delete/', views.toDelete, name='task_delete'),
]