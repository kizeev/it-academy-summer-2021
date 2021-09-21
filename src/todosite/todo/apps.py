from django.apps import AppConfig


class TodoConfig(AppConfig):
    """Конфигурация приложения."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'todo'
    verbose_name = 'Список дел'
