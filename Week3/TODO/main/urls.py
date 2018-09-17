from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.todos),
    path('1/completed/',views.completed)
   ]