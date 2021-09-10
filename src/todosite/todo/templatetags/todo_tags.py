from django import template
from django.db.models import Count

from ..models import Category, Task

register = template.Library()


@register.inclusion_tag('todo/list_categories.html')
def show_categories():
    """Функция для показа списка категорий и количества задач в каждой из них."""
    categories = Category.objects.order_by('category_name').annotate(cnt=Count('task'))
    return {'categories': categories}


@register.simple_tag
def get_tags():
    """Функция для показа всех тегов."""
    return Task.tags.all()
