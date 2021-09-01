from django.urls import path
from .views import *


urlpatterns = [
    path('', category_task_list),
    path('category/<int:category_id>/', get_category),
]
