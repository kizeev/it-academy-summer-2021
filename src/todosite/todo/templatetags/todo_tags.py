from datetime import date, timedelta
from django import template
from django.db.models import Count

from ..models import Category, Task

register = template.Library()


@register.inclusion_tag('todo/list_categories.html')
def show_categories():
    """Отображение списка категорий и количества задач в каждой из них."""
    categories = Category.objects \
        .order_by('category_name') \
        .filter(task__completed=False) \
        .annotate(cnt=Count('task'))
    return {'categories': categories}


@register.simple_tag
def get_tags():
    """Отображение всех тегов."""
    return Task.tags.all()


@register.simple_tag
def get_tasks():
    """Отображение всех задач."""
    return Task.objects.filter(completed=False)


@register.simple_tag()
def show_today():
    """Фильтр задач по дате 'сегодня'."""
    due_date = date.today()
    return Task.objects.filter(completed=False, due_date=due_date)


@register.simple_tag()
def show_tomorrow():
    """Фильтр задач по дате 'завтра'."""
    due_date = date.today() + timedelta(days=1)
    return Task.objects.filter(completed=False, due_date=due_date)


@register.simple_tag()
def show_week():
    """Фильтр задач по дате 'неделя'."""
    today = date.today()
    due_date = date.today() + timedelta(days=7)
    return Task.objects.filter(completed=False, due_date__range=(today, due_date))


@register.simple_tag()
def show_expired():
    """Фильтр задач с истекшим сроком выполнения."""
    today = date.today()
    return Task.objects.filter(completed=False, due_date__lt=today)


@register.simple_tag()
def show_completed():
    """Фильтр выполненных задач."""
    return Task.objects.filter(completed=True)
