from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .forms import TaskForm
from .models import Category, Task


class Home(ListView):
    """Класс для представления списка задач на странице."""
    model = Task
    template_name = 'todo/home.html'
    context_object_name = 'tasks'
    extra_context = {'title': 'Главная'}

    def get_queryset(self):
        return Task.objects.filter()  # здесь в скобках можно указать выборку


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
    """Функция просмотра выбранной задачи."""
    task_item = get_object_or_404(Task, pk=task_id)  # вернуть задачу, если ее нет - ошибку 404
    return render(request, 'todo/view_task.html', {'task_item': task_item})


def add_task(request):
    """Функция добавления новой задачи."""
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect(task)
    else:
        form = TaskForm()
    return render(request, 'todo/add_task.html', {'form': form})
