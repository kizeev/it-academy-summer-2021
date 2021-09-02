from django.shortcuts import render
from .models import Category, Task


def category_task_list(request):
    """Функция отображения категорий и задач на домошней странице сайта."""
    tasks = Task.objects.all()
    categories = Category.objects.all()
    return render(
        request,
        'todo/category_task_list.html',
        {'tasks': tasks, 'categories': categories, 'title': 'Список задач'},
    )


def get_category(request, category_id):
    """Функция отображения задач по выбранной категории."""
    tasks = Task.objects.filter(task_category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    return render(
        request,
        'todo/category.html',
        {'tasks': tasks, 'categories': categories, 'category': category, 'title': 'Список задач'},
    )
