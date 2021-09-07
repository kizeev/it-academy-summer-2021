from django.urls import path
from .views import *


urlpatterns = [
    path('', category_task_list, name='home'),
    path('category/<int:category_id>/', get_category, name='category'),
    path('task/<int:task_id>/', view_task, name='view_task'),
    path('task/add-task/', add_task, name='add_task'),
]
