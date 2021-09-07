from django.urls import path
from .views import *


urlpatterns = [
    path('', HomeTasks.as_view(), name='home'),
    path('category/<int:category_id>/', TasksByCategory.as_view(), name='category'),
    path('task/<int:task_id>/', ViewTask.as_view(), name='view_task'),
    path('task/add-task/', AddTask.as_view(), name='add_task'),
]
