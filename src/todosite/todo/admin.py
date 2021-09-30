from django.contrib import admin
from .models import Category, Task

admin.site.register(Category)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """Настройка отображения модели Task на сайте администрирования."""
    list_display = (
        'task_name',
        'task_category',
        'created',
        'due_date',
        'completed',
        'tags',
    )
    list_filter = ('task_category', 'created', 'due_date', 'completed', 'tags')
    search_fields = ('task_name',)
