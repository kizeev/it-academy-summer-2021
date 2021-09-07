from django import template
from django.db.models import Count

from ..models import Category

register = template.Library()


@register.simple_tag
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('todo/list_categories.html')
def show_categories():
    # categories = Category.objects.all()
    categories = Category.objects.annotate(cnt=Count('task'))  # количество задач в категории
    return {'categories': categories}
