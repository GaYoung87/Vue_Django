from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.todo_create, name='todo_create'),
    path('todos/<int:todo_id>/', views.todo_update_delete),
    path('users/<int:user_id>/', views.user_detail),
]