from django.shortcuts import render, get_object_or_404
from .models import Category, Task


def category_task_list(request):
    """Функция отображения категорий и задач на домошней странице сайта."""
    tasks = Task.objects.all()
    return render(
        request,
        'todo/home.html',
        {'tasks': tasks, 'title': 'Список задач'},
    )


def get_category(request, category_id):
    """Функция отображения задач по выбранной категории."""
    tasks = Task.objects.filter(task_category_id=category_id)
    category = Category.objects.get(pk=category_id)
    return render(
        request,
        'todo/category.html',
        {'tasks': tasks, 'category': category, 'title': 'Список задач'},
    )


def view_task(request, task_id):
    # task_item = Task.objects.get(pk=task_id)
    task_item = get_object_or_404(Task, pk=task_id)
    return render(request, 'todo/view_task.html', {'task_item': task_item})
