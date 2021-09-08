from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from .forms import TaskForm, UserRegisterForm, UserLoginForm
from .models import Category, Task


class HomeTasks(ListView):
    """Класс для представления списка задач на странице."""
    model = Task
    template_name = 'todo/home.html'
    context_object_name = 'tasks'
    extra_context = {'title': 'Главная'}
    paginate_by = 2

    def get_queryset(self):
        return Task.objects.filter()  # здесь в скобках можно указать выборку


class TasksByCategory(ListView):
    """Класс для представления списка задач по категориям."""
    model = Task
    template_name = 'todo/home.html'
    context_object_name = 'tasks'
    allow_empty = False

    def get_queryset(self):
        """Отображение выбранной категории в заголовке страницы."""
        return Task.objects.filter(task_category_id=self.kwargs['category_id'])

    def get_context_data(self, *, object_list=None, **kwargs):
        """Отображение задач по выбранной категории."""
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context


class ViewTask(DetailView):
    """Класс для представления выбранной задачи."""
    model = Task
    pk_url_kwarg = 'task_id'
    template_name = 'todo/view_task.html'
    context_object_name = 'task_details'


class AddTask(CreateView):
    """Класс для создания новой задачи."""
    form_class = TaskForm
    template_name = 'todo/add_task.html'


def register(request):
    """Функция для регистрации на сайте."""
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'todo/register.html', {'form': form})


def user_login(request):
    """Функция для авторизации на сайте."""
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Вы успешно вошли в учетную запись')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserLoginForm()
    return render(request, 'todo/login.html', {'form': form})


def user_logout(request):
    """Функция для из учетной записи."""
    logout(request)
    return redirect('login')
