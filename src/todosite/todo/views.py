from datetime import date, timedelta
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import login, logout
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from taggit.models import Tag
from .forms import TaskForm, CategoryForm, UserRegisterForm, UserLoginForm, EmailForm
from .models import Category, Task


class HomeTasks(ListView):
    """Представление списка задач на главной странице."""
    model = Task
    template_name = 'todo/home.html'
    context_object_name = 'tasks'
    extra_context = {'title': 'Главная'}
    paginate_by = 10

    def get_queryset(self):
        return Task.objects.filter()  # здесь в скобках можно указать выборку


class TasksByCategory(ListView):
    """Представление списка задач по категориям."""
    model = Task
    template_name = 'todo/tasks_by_category.html'
    context_object_name = 'tasks'
    allow_empty = True
    paginate_by = 10

    def get_queryset(self):
        """Отображение задач по выбранной категории."""
        return Task.objects.filter(task_category_id=self.kwargs['category_id'])

    def get_context_data(self, *, object_list=None, **kwargs):
        """Отображение выбранной категории в заголовке страницы."""
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context


class ViewTask(DetailView):
    """Отображение выбранной задачи."""
    model = Task
    pk_url_kwarg = 'task_id'
    template_name = 'todo/view_task.html'
    context_object_name = 'task_details'


class AddTask(CreateView):
    """Создание новой задачи."""
    form_class = TaskForm
    template_name = 'todo/add_task.html'


class EditTask(UpdateView):
    """Редактирование существующей задачи."""
    model = Task
    pk_url_kwarg = 'task_id'
    template_name = 'todo/edit_task.html'
    form_class = TaskForm
    success_url = '/todo/'


class DeleteTask(DeleteView):
    """Удаление выбранной задачи."""
    model = Task
    template_name = 'todo/delete_task.html'
    success_url = '/todo/'
    pk_url_kwarg = 'task_id'


class AddCategory(CreateView):
    """Создание новой категории."""
    form_class = CategoryForm
    template_name = 'todo/add_category.html'


def register(request):
    """Регистрация на сайте."""
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
    return render(request, 'registration/register.html', {'form': form})


def user_login(request):
    """Авторизация на сайте."""
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Вы успешно вошли в учетную запись')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка авторизации')
    else:
        form = UserLoginForm()
    return render(request, 'registration/login.html', {'form': form})


def user_logout(request):
    """Выход из учетной записи."""
    logout(request)
    return redirect('login')


def email_send(request):
    """Отправка электронной почты."""
    if request.method == 'POST':
        form = EmailForm(data=request.POST)
        if form.is_valid():
            mail = send_mail(
                form.cleaned_data['subject'],
                form.cleaned_data['content'],
                'natusutprimussim@gmail.com',
                ['kizalvic@gmail.com'],
                fail_silently=False,
            )
            if mail:
                messages.success(request, 'Письмо отправлено')
                return redirect('home')
            else:
                messages.error(request, 'Ошибка отправки')
    else:
        form = EmailForm()
    return render(request, 'todo/mail.html', {'form': form})


def tasks_by_tag(request, tag_id=None):
    """Фильтр задач по тегам."""
    tasks_list = Task.objects.all()
    tag = None
    if tag_id:
        tag = get_object_or_404(Tag, id=tag_id)
        tasks_list = tasks_list.filter(tags__in=[tag])

    paginator = Paginator(tasks_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'todo/tasks_by_tags.html', {'tag': tag, 'page_obj': page_obj})


def tasks_by_date(request, requested_date):
    """Фильтр задач по дате выполнения."""
    tasks_list = Task.objects.all()

    if requested_date == 'today':
        requested_date = date.today()
        tasks_list = tasks_list.filter(due_date=requested_date)
        title = 'Сегодня'
    elif requested_date == 'tomorrow':
        requested_date = date.today() + timedelta(days=1)
        tasks_list = tasks_list.filter(due_date=requested_date)
        title = 'Завтра'
    elif requested_date == 'week':
        requested_date = date.today() + timedelta(days=7)
        tasks_list = tasks_list.filter(due_date__lte=requested_date)
        title = 'Эта неделя'
    elif requested_date == 'all':
        tasks_list = tasks_list
        title = 'Все'

    paginator = Paginator(tasks_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'todo/tasks_by_date.html', {'title': title, 'page_obj': page_obj})
