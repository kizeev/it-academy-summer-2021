from django.contrib import admin
from .models import CategoryTask, Task


admin.site.register(CategoryTask)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """Настройка отображения модели Task на сайте администрирования."""
    list_display = ('task_name', 'category_task', 'created', 'priority')
    list_filter = ('category_task', 'created', 'priority')
    search_fields = ('task_name',)

