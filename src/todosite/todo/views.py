from django.shortcuts import render
from .models import CategoryTask, Task


def category_task_list(request):
    """Функция отображения категорий и задач на домошней странице сайта."""
    tasks = Task.objects.all()
    categories = CategoryTask.objects.all()
    return render(request, 'index.html', {'tasks': tasks, 'categories': categories})
