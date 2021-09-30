from datetime import date, timedelta
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import login, logout
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from taggit.models import Tag
from .forms import TaskForm, CategoryForm, UserRegisterForm, UserLoginForm, EmailForm
from .models import Category, Task


class HomeTasks(ListView):
    """Представление списка задач на главной странице."""
    model = Task
    template_name = 'todo/home.html'
    context_object_name = 'tasks'
    extra_context = {'title': 'Все задачи'}
    paginate_by = 10

    def get_queryset(self):
        return Task.objects.filter(completed=False)  # здесь в скобках можно указать выборку


class TasksByCategory(ListView):
    """Представление списка задач по категориям."""
    model = Task
    template_name = 'todo/home.html'
    context_object_name = 'tasks'
    allow_empty = True
    paginate_by = 10

    def get_queryset(self):
        """Отображение задач по выбранной категории."""
        return Task.objects\
            .filter(task_category_id=self.kwargs['category_id'])\
            .filter(completed=False)

    def get_context_data(self, *, object_list=None, **kwargs):
        """Отображение выбранной категории в заголовке страницы."""
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context


class AddTask(CreateView):
    """Создание новой задачи."""
    form_class = TaskForm
    template_name = 'todo/add_task.html'
    success_url = '/todo/'


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


class SearchTasks(ListView):
    model = Task
    template_name = 'todo/home.html'
    extra_context = {'title': 'Результаты поиска'}
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('search')
        tasks_list = Task.objects.filter(task_name__icontains=query)
        return tasks_list


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
    return render(request, 'todo/register.html', {'form': form})


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
    return render(request, 'todo/login.html', {'form': form})


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

    title = 'Тег: ' + str(tag)
    paginator = Paginator(tasks_list, 10)
    page_number = request.GET.get('page')
    object_list = paginator.get_page(page_number)
    return render(
        request,
        'todo/home.html',
        {'tag': tag, 'object_list': object_list, 'title': title}
    )


def tasks_by_date(request, requested_date):
    """Фильтр задач по дате выполнения."""
    tasks_list = Task.objects.filter(completed=False)
    today = date.today()

    if requested_date == 'today':
        requested_date = today
        tasks_list = tasks_list.filter(due_date=requested_date)
        title = 'Сегодня'
    elif requested_date == 'tomorrow':
        requested_date = today + timedelta(days=1)
        tasks_list = tasks_list.filter(due_date=requested_date)
        title = 'Завтра'
    elif requested_date == 'week':
        requested_date = today + timedelta(days=7)
        tasks_list = tasks_list.filter(due_date__range=(today, requested_date))
        title = 'Эта неделя'
    elif requested_date == 'all':
        tasks_list = tasks_list
        title = 'Все'
    elif requested_date == 'expired':
        tasks_list = tasks_list.filter(due_date__lt=today)
        title = 'Просроченные'

    paginator = Paginator(tasks_list, 10)
    page_number = request.GET.get('page')
    object_list = paginator.get_page(page_number)
    return render(request, 'todo/home.html', {'title': title, 'object_list': object_list})


def change_completed_status(request, task_id):
    """
    Изменить статус выполнения задачи.

    После изменения статуса возвращает на предыдущую страницу.
    """
    task = Task.objects.filter(id=task_id).get()
    if task.completed:
        task.completed = False
    else:
        task.completed = True
    task.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def completed_tasks(request):
    """Выбрать завершенные задачи."""
    tasks_list = Task.objects.filter(completed=True)
    paginator = Paginator(tasks_list, 10)
    page_number = request.GET.get('page')
    object_list = paginator.get_page(page_number)
    return render(
        request,
        'todo/home.html',
        {'object_list': object_list, 'title': 'Выполненные'}
    )
