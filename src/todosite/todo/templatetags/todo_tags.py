from datetime import date, timedelta
from django import template
from django.db.models import Count

from ..models import Category, Task

register = template.Library()


@register.inclusion_tag('todo/list_categories.html')
def show_categories():
    """Функция для отображения списка категорий и количества задач в каждой из них."""
    categories = Category.objects.order_by('category_name').annotate(cnt=Count('task'))
    return {'categories': categories}


@register.simple_tag
def get_tags():
    """Функция для отображения всех тегов."""
    return Task.tags.all()


@register.simple_tag
def get_tasks():
    """Функция для отображения всех задач."""
    return Task.objects.all()


@register.simple_tag()
def show_today():
    """Фильтр задач по дате 'сегодня'."""
    return Task.objects.all().filter(due_date=date.today())


@register.simple_tag()
def show_tomorrow():
    """Фильтр задач по дате 'завтра'."""
    return Task.objects.all().filter(due_date=date.today() + timedelta(days=1))


@register.simple_tag()
def show_week():
    """Фильтр задач по дате 'неделя'."""
    return Task.objects.all().filter(due_date__lte=date.today() + timedelta(days=7))
