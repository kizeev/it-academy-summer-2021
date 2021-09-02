from django.urls import path
from .views import *


urlpatterns = [
    path('', category_task_list, name='todo'),
    path('category/<int:category_id>/', get_category, name='category'),
]
