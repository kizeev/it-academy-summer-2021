from django.urls import path
from .views import *


urlpatterns = [
    path('', HomeTasks.as_view(), name='home'),
    path('category/<int:category_id>/', TasksByCategory.as_view(), name='category'),
    path('tag/<slug:tag_slug>/', tasks_by_tag, name='tasks_by_tag'),
    path('task/<int:task_id>/', ViewTask.as_view(), name='view_task'),
    path('task/add-task/', AddTask.as_view(), name='add_task'),
    path('task/add-category/', AddCategory.as_view(), name='add_category'),
    path('register', register, name='register'),
    path('login', user_login, name='login'),
    path('logout', user_logout, name='logout'),
    path('mail', email_send, name='mail'),
]
