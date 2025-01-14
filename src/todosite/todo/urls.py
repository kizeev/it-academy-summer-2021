from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeTasks.as_view(), name='home'),
    path('category/<int:category_id>/', TasksByCategory.as_view(), name='tasks_by_category'),
    path('date/<str:requested_date>/', tasks_by_date, name='tasks_by_date'),
    path('tag/<int:tag_id>/', tasks_by_tag, name='tasks_by_tag'),
    path('completed/', completed_tasks, name='completed_tasks'),
    path('task/<int:task_id>/edit/', EditTask.as_view(), name='edit_task'),
    path('task/<int:task_id>/delete/', DeleteTask.as_view(), name='delete_task'),
    path('task/add-task/', AddTask.as_view(), name='add_task'),
    path('task/<int:task_id>/complete/', change_completed_status, name='complete_task'),
    path('search/', SearchTasks.as_view(), name='search_task'),
    path('category/add-category/', AddCategory.as_view(), name='add_category'),
]
