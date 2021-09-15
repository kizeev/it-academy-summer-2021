from django.urls import path
from .views import *


urlpatterns = [
    path('', HomeTasks.as_view(), name='home'),
    path('category/<int:category_id>/', TasksByCategory.as_view(), name='tasks_by_category'),
    path('date/<str:requested_date>/', tasks_by_date, name='tasks_by_date'),
    path('tag/<int:tag_id>/', tasks_by_tag, name='tasks_by_tag'),
    path('task/<int:task_id>/', ViewTask.as_view(), name='view_task'),
    path('task/<int:task_id>/edit/', EditTask.as_view(), name='edit_task'),
    path('task/<int:task_id>/delete/', DeleteTask.as_view(), name='delete_task'),
    path('task/add-task/', AddTask.as_view(), name='add_task'),
    path('task/add-category/', AddCategory.as_view(), name='add_category'),
    path('register', register, name='register'),
    path('login', user_login, name='login'),
    path('logout', user_logout, name='logout'),
    path('mail', email_send, name='mail'),
]
