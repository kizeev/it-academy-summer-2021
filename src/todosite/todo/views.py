from django.shortcuts import render
from . models import CategoryTask, Task


def task_list(request):
    """Функция отображения задач на домошней странице сайта."""
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})


def category_task_list(request):
    """Функция отображения категорий задач на домошней странице сайта."""
    categories = CategoryTask.category_name.all()
    return render(request, 'index.html', {'categories': categories})
